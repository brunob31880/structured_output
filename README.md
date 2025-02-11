# Projet de parsing de sortie avec LangChain et Ollama

Ce projet utilise LangChain, Ollama et Pydantic pour parser la sortie d'un modèle de langage (LLM) en réponse à une requête utilisateur. Le modèle utilisé est `llama3.1`, et la sortie est parsée en un format structuré utilisant Pydantic.

## Prérequis

Avant de pouvoir exécuter ce projet, assurez-vous d'avoir installé les dépendances suivantes :

- Python 3.8 ou supérieur
- Les bibliothèques Python suivantes :
  - `langchain`
  - `pydantic`
  - `langchain-ollama`

Vous pouvez installer les dépendances en utilisant `pip` :

```bash
pip install langchain pydantic langchain-ollama
```

## Structure du projet

Le projet est composé d'un script Python qui effectue les étapes suivantes :

1. **Définition du modèle LLM** : Le modèle `llama3.1` est utilisé via `OllamaLLM`.
2. **Définition du modèle Pydantic** : Un modèle Pydantic est utilisé pour parser la sortie du LLM en une structure de données Python.
3. **Création du prompt** : Un prompt est créé avec des instructions de formatage pour guider le LLM à produire une sortie structurée.
4. **Exécution de la requête** : La requête utilisateur est exécutée via une chaîne (`chain`) qui combine le prompt, le modèle LLM, et le parser.
5. **Affichage des résultats** : Les résultats parsés sont affichés.

## Utilisation

Pour exécuter le script, utilisez la commande suivante :

```bash
python script.py
```

### Exemple de sortie

Si la requête utilisateur est "The Fable of the Fox and the Crow", la sortie pourrait ressembler à ceci :

```
Names: ['Fox', 'Crow']
Places: ['forest']
```
