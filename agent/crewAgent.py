#Bibliotecas para craição de Agent
from crewai import Crew, Process, Agent, Task , LLM
import os
from langchain_community.tools import DuckDuckGoSearchResults
from crewai_tools import ScrapeWebsiteTool
from crewai.tools import BaseTool
from pydantic import Field
import json
import sys
from dotenv import load_dotenv
from datetime import datetime

# Configuração de Saída UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Carrega variáveis de ambiente
load_dotenv()

## Tool de Busca DuckGOSearch ##
class SearchTool(BaseTool):
    name: str = "Search"
    description: str = "Use para buscar informações atuais em sites de notícias e blogs. Ideal para descobrir tendências ou checar fatos recentes."
    search: DuckDuckGoSearchResults = Field(default_factory=lambda: DuckDuckGoSearchResults(output_format="json", max_results=10, region='pt-br'))

    def _run(self, query: str) -> str:
        try:
            results = self.search.run(query)
            if isinstance(results, str):
                try:
                    results = json.loads(results)
                except:
                    return results
            response = [
                {
                    "title": item.get("title"),
                    "link": item.get("link"),
                    "snippet": item.get("snippet")
                }
                for item in results if "title" in item and "link" in item
            ]
            return json.dumps(response, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"Erro ao realizar a busca: {str(e)}"

# ATENÇÃO: mudei o nome para não conflitar
class DoctorAgent:
    def __init__(self, api_key=None):
        token = api_key if api_key else os.getenv('GITHUB_API_KEY')
        endpoint = "https://models.github.ai/inference"

        self.llm = LLM(
            model="openai/gpt-4.1",
            base_url=endpoint,
            api_key=token,
            temperature=0.2,
            max_tokens=32768,
            publisher= "openai"
        )

        # Instanciação Agente Médico
        self.medic = Agent(
            role="Médico",
            goal="Analisar os sintomas descritos pelo paciente e gerar um laudo médico claro, estruturado e embasado em fontes confiáveis.",
            backstory="""
            Você é um médico especializado em diagnósticos preliminares com apoio de informações da internet. Seu papel é receber os sintomas relatados por um paciente e, com base neles, fazer uma análise cuidadosa.

            Utilize fontes confiáveis e gere recomendações claras.
            """,
            llm=self.llm
        )

        # Tasks
        self.pacient_analyze = Task(
            description="""
        Analisar cuidadosamente os sintomas relatados pelo paciente e realizar uma análise médica preliminar com base nessas informações.
        Utilizar ferramentas de busca web para investigar possíveis causas, condições associadas e contextos relevantes.
        """,
            expected_output="""
        Um parecer médico preliminar sobre o tema {topic}, abordando os principais sintomas descritos pelo paciente,
        com explicações claras e objetivas. A resposta deve ser semelhante à de um médico durante uma consulta clínica,
        sendo firme, empática e informativa, sem emitir um diagnóstico definitivo.
        """,
            agent=self.medic,
            tools=[ScrapeWebsiteTool(), SearchTool()]
        )

        self.clinical_analysis = Task(
            description="""
        Com base nos sintomas analisados, elaborar um laudo médico estruturado e profissional.
        O laudo deve oferecer sugestões baseadas em evidências, prezando pela clareza e apoio ao paciente.

        O documento deve usar:
        - Cabeçalhos (Markdown `#`, `##`, `###`).
        - Linhas horizontais (`---`) para separar seções.
        - Listas com marcadores claros (`-` ou `*`).
        - Texto em **negrito** e _itálico_ para enfatizar pontos-chave.
        - Blocos de destaque, quando necessário, com citações Markdown (`> texto`).

        """,
        expected_output="""
        Um laudo médico contendo bem estilizado e com visual elegante contendo os seguintes pontos :
        - Resumo dos sintomas apresentados
        - Possíveis causas ou diagnósticos diferenciais
        - Indicação de medicamentos (nome, posologia, duração)
        - Recomendações clínicas e orientações de cuidado
        - Observações importantes (como evitar automedicação ou procurar atendimento emergencial)
        - Fontes utilizadas (se aplicável)


        """,
            agent=self.medic
        )

        # Monta a Crew
        self.crew = Crew(
            agents=[self.medic],
            tasks=[self.pacient_analyze, self.clinical_analysis],
            verbose=True,
            process=Process.sequential
        )

    def run(self, entrada: str):
        inputs = {
            'topic': entrada,
            'current_year': str(datetime.now().year)
        }
        resultado = self.crew.kickoff(inputs=inputs)
        return resultado
