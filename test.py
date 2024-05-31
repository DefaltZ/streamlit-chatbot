from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import PromptTemplate


llm = Ollama(model="phi3:mini")
prompt = PromptTemplate.from_template("""You are a terse and grumpy cartographer. You insult people who ask obvious questions but still always 
                                      answer anyways.
                                      
                                      now answer the following question:
                                      
                                      Question: {question}
""")

output = (prompt | llm).stream({"question": "why do you do what you do?"})
for chunk in output:
    print(chunk, flush=True, end="")