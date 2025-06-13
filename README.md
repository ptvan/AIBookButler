# AIBookButler

This repo contains a book recommendation system powered by [LangChain](https://python.langchain.com/docs/introduction/).

## Data

The Kaggle dataset [7K Books with metadata](https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata) is used for training

## Code

Raw CSV from Kaggle is cleaned, resulting in ~5000 rows of data. This text is split and loaded into a Chroma vector database using an English text embedding (I used [nomic-embed-text](https://ollama.com/search?q=embed))

## Usage

The system can be served locally through [Ollama](https://ollama.com/) though most LLMs should work. A query can be entered using [2_text_classification.ipynb](2_text_classification.ipynb) (eg. "a book about sailing"), which returns top hits from the database using a similarity search. 

## Acknowledgements

Thank you to Dan Sommer for very useful LLM discussions

## TO-DO

- Replace querying code with a more pleasant and convenient frontend
- Benchmark accuracy between different embeddings and/or LLMs
