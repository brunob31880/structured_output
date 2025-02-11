from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from typing import List, Optional
from langchain_ollama import OllamaLLM

# Définition du modèle utilisé
model_name = "mistral-nemo"
model = OllamaLLM(model=model_name)

# Définition du prompt
prompt = PromptTemplate(
    template="Answer the user query.\n{query}\n",
    input_variables=["query"],
)

# Pipeline d'exécution
chain = prompt | model 

# Requête utilisateur
query = "The Fable of the Fox and the Crow"

# Exécution de la requête
result = chain.invoke({"query": query})
print(f"Result {result}")
