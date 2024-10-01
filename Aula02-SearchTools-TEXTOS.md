# Ferramentas de Busca

| Tool/Toolkit                                                                              | Free/Paid                    | Return Data                                           |
|:----------------------------------------------------------------------------------------- |:----------------------------:|:-----------------------------------------------------:|
| [Bing Search](https://python.langchain.com/v0.2/docs/integrations/tools/bing_search/)     | Paid                         | URL, Snippet, Title                                   |
| [Brave Search](https://python.langchain.com/v0.2/docs/integrations/tools/brave_search/)   | Free                         | URL, Snippet, Title                                   |
| [DuckDuckgoSearch](https://python.langchain.com/v0.2/docs/integrations/tools/ddg/)        | Free                         | URL, Snippet, Title                                   |
| [Exa Search](https://python.langchain.com/v0.2/docs/integrations/tools/exa_search/)       | 1000 free searches/month     | URL, Author, Title, Published Date                    |
| [Google Search](https://python.langchain.com/v0.2/docs/integrations/tools/google_search/) | Paid                         | URL, Snippet, Title                                   |
| [Google Serper](https://python.langchain.com/v0.2/docs/integrations/tools/google_serper/) | Free                         | URL, Snippet, Title, Search Rank, Site Links          |
| [Mojeek Search](https://python.langchain.com/v0.2/docs/integrations/tools/mojeek_search/) | Paid                         | URL, Snippet, Title                                   |
| [SearchApi](https://python.langchain.com/v0.2/docs/integrations/tools/searchapi/)         | 100 Free Searches on Sign Up | URL, Snippet, Title, Search Rank, Site Links, Authors |
| [SearxNG Search](https://python.langchain.com/v0.2/docs/integrations/tools/searx_search/) | Free                         | URL, Snippet, Title, Category                         |
| [SerpAPI](https://python.langchain.com/v0.2/docs/integrations/tools/serpapi/)             | 100 Free Searches/Month      | Answer                                                |
| [Tavily Search](https://python.langchain.com/v0.2/docs/integrations/tools/tavily_search/) | 1000 free searches/month     | URL, Content, Title, Images, Answer                   |
| [You.com Search](https://python.langchain.com/v0.2/docs/integrations/tools/you/)          | Free for 60 days             | URL, Title, Page Content                              |
| https://python.langchain.com/v0.2/docs/integrations/tools/                                |                              |                                                       |

### Configurando nossa primeira ferramenta LangChain: DuckDuckGo

DuckDuckGo é um mecanismo de busca que enfatiza a proteção da privacidade dos usuários. Diferentemente de outros mecanismos de busca, o DuckDuckGo não rastreia o histórico de busca de seus usuários, o que significa que ele não cria ou mantém um perfil pessoal de seus usuários.

Ele tem uma biblioteca Python que precisamos instalar para usar o mecanismo de busca. Ele é instalável via `pip`:

```python
pip install duckduckgo-search
```

Além disso, precisamos importar a ferramenta DuckDuckGo da `langchain`:

```python
from langchain_community.tools import DuckDuckGoSearchRun
ddg_search = DuckDuckGoSearchRun()
ddg_search.run("Prompt")
```

O método `DuckDuckGoSearchRun()`por si só já permite navegar na internet sem precisar interagir com nenhum LLM. Vamos ver um exemplo simples:

_![Captura de tela da execução ddg_search.run() para navegar na internet com DuckDuckGo](https://images.datacamp.com/image/upload/v1701876250/image_e9df105d39.png)_

## Explorando outras ferramentas de navegação

Depois de aprendermos a configurar nossa primeira ferramenta, configurar as demais deve ser bem simples, já que todas seguem a mesma estrutura.

### Ferramenta Google Serper

O Google Serper é uma API de pesquisa do Google de baixo custo que nos permite navegar na Internet como DuckDuckGo.

Para esta ferramenta, precisamos de uma chave de API que podemos obter criando uma conta gratuita em [https://serper.dev/](https://serper.dev/) .

_![Captura de tela da página principal da API do Google Serper](https://images.datacamp.com/image/upload/v1701876250/image_fdab27e410.png)_

Quando estivermos em nossa conta Serper, poderemos ver a opção de **chave de API** no painel esquerdo:

_![Captura de tela de uma página de conta na API do Google Serper](https://images.datacamp.com/image/upload/v1701876250/image_4c5eb8f6a1.png)_

Ao clicar nele, obteremos a chave de API que podemos facilmente copiar e integrar em nossos scripts Python:

_![Captura de tela da geração da chave de API na página do Google Serper](https://images.datacamp.com/image/upload/v1701876250/image_4a613d9a03.png)_

Voltando ao código, podemos facilmente importar a chave para o nosso ambiente:

```python
serper_api_key = os.environ["SERPER_API_KEY"]
```

Para usar a API do Google Serper, precisamos primeiro instalar a biblioteca Python necessária ( `pip install google-serp-api`). Além disso, precisamos importar a `GoogleSerper`ferramenta da `langchain`biblioteca:

```python
from langchain.utilities import GoogleSerperAPIWrapper 
google_search = GoogleSerperAPIWrapper()
google_search.run("Prompt")
```

### Ferramenta Wikipédia

Vamos complementar nosso conjunto de Ferramentas com as fontes conhecidas da Wikipédia, seguindo o mesmo processo das Ferramentas anteriores.

O primeiro passo é instalar a biblioteca `wikipedia` via `pip`( `pip install wikipedia`), e carregar os módulos necessários da biblioteca LangChain. Esta ferramenta na verdade precisa de dois módulos devido à arquitetura da API da Wikipedia:

```python
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

print(wikipedia.run("Palmeiras?"))
```

### Ferramenta do YouTube

Por fim, achei muito interessante integrar as fontes do YouTube para que o modelo tenha uma capacidade adicional de responder na forma de vídeos, não apenas texto escrito. Seguindo o mesmo procedimento de antes:

```python
#pip install --upgrade --quiet youtube_search

from langchain_community.tools import YouTubeSearchTool

youtube = YouTubeSearchTool()
```

