from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from typing import Optional
from langchain_ollama import OllamaLLM

# Définition du modèle utilisé
model_name = "mistral-nemo"
model = OllamaLLM(model=model_name)

# Définition du modèle Pydantic pour parser la sortie
class SentimentAnalysis(BaseModel):
    sentiment: str = Field(description="Sentiment of the text (e.g., positive, negative, neutral)")
    confidence: Optional[float] = Field(default=None, description="Confidence score of the sentiment analysis")

class Output(BaseModel):
    properties: SentimentAnalysis

# Création du parser
parser = PydanticOutputParser(pydantic_object=Output)

# Définition du prompt avec les instructions de formatage du parser
prompt = PromptTemplate(
    template="Analyze the sentiment of the following text.\n{format_instructions}\nText: {query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Pipeline d'exécution
chain = prompt | model | parser

# Requête utilisateur
query = "I love the sunny weather today! It makes me feel so happy and energized."

# Exécution de la requête
result = chain.invoke({"query": query})
print(f"Result: {result}")

# Accès aux résultats
print("Sentiment:", result.properties.sentiment)
print("Confidence:", result.properties.confidence)
