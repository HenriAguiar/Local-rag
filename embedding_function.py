from langchain_community.embeddings import OllamaEmbeddings

def get_embedding_function():

    embeddings = OllamaEmbeddings(
        base_url="http://localhost:11434",
        model="mxbai-embed-large",

    )

    return embeddings