from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate # we need this for dynamic prompting
# ChatPromptTemplate is a LangChain class used to create dynamic chat prompts using placeholders. 
# It allows us to pass different inputs at runtime instead of hardcoding prompts.

from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(model="openai/gpt-oss-20b")
out = StrOutputParser()

# ans = llm.invoke("who is the pm of india?")

# prompt = [
#     {"role": "system", "content": "you are translator that translate english into hindi"},
#     {"role": "user", "content": "my name is kanak"}
# ]

prompts = ChatPromptTemplate.from_messages([
    {"role":"system", "content":"you are a translator and translate input in {language}"},#system prompt
    {"role":"user", "content":"{query}"}
])

final_promts = prompts.format_messages(language = "Korean", query="i love you")
# final prompts method is a little big 

def transform(result : str) :
    return result.upper()

chains = prompts | llm | out | transform

res = chains.invoke({"language": "Hindi", "query": "hello kanak"})
print(res)

