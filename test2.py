from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from typing import List
from langchain_ollama import OllamaLLM
from langchain_core.exceptions import OutputParserException
import logging

# Configuration des logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Définition du modèle utilisé
model_name = "mistral-nemo"
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

# Requête utilisateur
query = "The Fable of the Fox and the Crow"

# Validation de la requête
if not query or not query.strip():
    raise ValueError("Query cannot be empty.")

# Formatage du prompt
_input = prompt.format_prompt(query=query)
logger.info("Input: %s", _input.to_string())

try:
    # Exécution de la requête
    output = model(_input.to_string())
    logger.info("Output: %s", output)

    # Parsing de la sortie
    result = parser.parse(output)
    logger.info("Result: %s", result)

    # Affichage des résultats
    print("Names:", result.properties.names)
    print("Places:", result.properties.places)
except OutputParserException as e:
    logger.error(f"Parsing error: {e}")
except Exception as e:
    logger.error(f"An error occurred: {e}")
