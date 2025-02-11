from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from typing import List, Optional
from langchain_ollama import OllamaLLM

# Définition du modèle utilisé
model_name = "llama3.1"
model = OllamaLLM(model=model_name)

# Définition du modèle Pydantic pour parser la sortie
class Properties(BaseModel):
    names: List[str] = Field(default_factory=list, min_items=1, description="List of character names")
    places: List[str] = Field(default_factory=list, description="List of places (can be empty)")

class Output(BaseModel):
    properties: Properties


# Création du parser
parser = PydanticOutputParser(pydantic_object=Output)

# Définition du prompt avec les instructions de formatage du parser
prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Pipeline d'exécution
chain = prompt | model | parser

# Requête utilisateur
query = "The Fable of the Fox and the Crow"

# Exécution de la requête
result = chain.invoke({"query": query})

# Accès aux résultats
print("Names:", result.properties.names)
print("Places:", result.properties.places)
