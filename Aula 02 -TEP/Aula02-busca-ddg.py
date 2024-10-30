from langchain_community.tools import DuckDuckGoSearchRun
ddg_search = DuckDuckGoSearchRun()
result = ddg_search.run( "Qual é a capital do Brasil")
print(result)