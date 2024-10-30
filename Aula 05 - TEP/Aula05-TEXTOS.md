# Aula 5 -Conceitos de RAG com Langchain e Langflow

Atividades com Agentes CREW AI

**Agentes de IA com CrewAI e Llama3 usando a API Groq**

Este exemplo demonstra como criar agentes de IA usando a biblioteca CrewAI, o modelo Llama3 e a API Groq em Python. O objetivo é fornecer uma estrutura básica para configurar e executar agentes de IA.

### Requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- Python 3.8 ou superior
- Biblioteca CrewAI
- Acesso à API Groq para o modelo Llama3
- pip para gerenciar pacotes Python

### Instalação

1. Clone o repositório:
   
   ```bash
   git clone https://github.com/viniciusds2020/ai_crewai_starter_template.git
   cd ai_crewai_starter_template
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   
   ```shell
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   
   ```shell
   pip install -r requirements.txt
   ```

### Configuração

1. Obtenha uma chave de API da Groq para acessar o modelo Llama3. Registre-se no site da Groq e siga as instruções para gerar a chave de API.

2. Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API:
   
   ```bash
   GROQ_API_KEY=your_api_key_here
   ```

Teste sua configuração para verificar se está carregando corretamente o arquivo .env

```python
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Verifica se a chave foi carregada corretamente
groq_api_key = os.getenv('GROQ_API_KEY')
if groq_api_key is None:
    print("A chave da API não foi carregada corretamente.")
else:
    print("Chave da API carregada:", groq_api_key)
```

### Uso

O arquivo principal `main.py` contém a lógica para inicializar e executar o agente de IA. Para iniciar o agente, execute:

```shell
python main.py
```

## Estrutura do Projeto

```
.
├── README.md
├── requirements.txt
├── main.py
└── .env
```

- `README.md`: Este arquivo de documentação.
- `requirements.txt`: Arquivo de dependências do Python.
- `main.py`: Script principal que inicializa e executa o agente de IA.
- `.env`: Arquivo contendo a chave de API da Groq.

Fiz alguns pequenos ajustes abaixo para facilar o uso. Revise seu arquivo.

Arquivo **agents.py**

```python
### Sistemas de multi-agentes de inteligencias artificiais

# Biblioteca
from crewai_tools import tool
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun

# Modelo LLM - Llama3 
llm = ChatGroq(temperature=0.7,
               groq_api_key='sua-chave-api-groq',
               model_name='llama-3.1-8b-instant') #novo modelo

#se for usar o GPT
#llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3)

# Ferramentas - Busca na internet com DuckDuckGo
@tool('DuckDuckGoSearchRun')
def search_tool(search_query: str):
  ''' Search the web for infotmation on a given topic'''
  return DuckDuckGoSearchRun().run(search_query)

# Topico do blog
topic = "Apple and AI in finance"

# Agentes
researcher = Agent(
    role = "Senior Researcher",
    goal = f"Explore trending technologies in {topic}.",
    backstory = "You are an innovative researher who follows the latest technology",
    verbose = True,
    tools = [search_tool],
    llm = llm,
)

writer = Agent(
    role = "Top Writer",
    goal = f"Create engaging content about {topic}. ",
    backstory = "You are an expert blogger who writes interesting articles.",
    verbose = True,
    tools = [search_tool],
    llm = llm,
)

# Tarefas
research_task = Task(
    description = f"Investigate the latest AI trends in {topic}.",
    expected_output = "A comprehensive 4 paragraphs long report on the latest AI trends.",
    tools = [search_tool],
    agent = researcher,
)

write_task = Task(
    description = f"Write an engaging article on {topic} that focuses on the latest trends.",
    expected_output = f"A comprehensive 4 paragraphs blog on {topic} in markdown format.",
    tools = [search_tool],
    agent = researcher,
    output_file = "my-blog.md"
)

# Orquestrador
crew = Crew(
    agents=[researcher, writer],
    tasks = [research_task, write_task]
)

result = crew.kickoff(
    inputs = {"topic": topic}
)
```

Vamos adaptar o projeto acima para pesquisar e redigir uma notícia com dados recentes sobre as queimadas em Mato Grosso.

Faça uma cópia do arquivo main.py para agente.py

Obs. Altere os prompts, de modo com que o resultado produzido seja em Porguês do Brasil, contudo, mantenha os roles definidos para os agentes ou verifique com mais cuidado a documentação em [crewAI Agents - crewAI](https://docs.crewai.com/core-concepts/Agents/#creating-an-agent).

Renomei também o `output_file = "news.md"`.

**Ok. Quando finalizar suba tudo para seu Git OK!**

## **Instalar o Langflow** [localmente](https://docs.langflow.org/getting-started-installation#ef364ee864c545649d248113ad7d3038 "Link direto para ef364ee864c545649d248113ad7d3038")

---

Cuidado

O Langflow  **requer que**  o Python versão 3.10 ou superior e  [o pip](https://pypi.org/project/pip/)  ou  [pipx](https://pipx.pypa.io/stable/installation/)  estejam instalados no seu sistema.

Instale o Langflow com pip:

`   1  python -m pip install langflow -U            `

Instale o Langflow com pipx:

`   1  pipx install langflow --python python3.10 --fetch-missing-python            `

O Pipx pode buscar a versão Python faltante para você com  `--fetch-missing-python`, mas você também pode instalar a versão Python manualmente. Use  `--force-reinstall` para garantir que você tenha a versão mais recente do Langflow e suas dependências.

## ⛓️ Execute [o Langflow](https://docs.langflow.org/getting-started-installation#d318c4d486b74f5383c45b4f6859dcaa "Link direto para ⛓️ Executar Langflow")

---

1. Para executar o Langflow, digite o seguinte comando.

`   1  python -m langflow run            `

2. Confirme se uma instância local do Langflow é iniciada visitando  o site `http://127.0.0.1:7860` em um navegador baseado em Chromium.

![](https://docs.langflow.org/assets/images/221680153-422d15086b005089f39efee126ea17d1.png)

## Exemplos de Fluxos no LANGFLOW

- TEP - Chat com Memória

- TEP - CrewAI

- TEP - PDF RAG
