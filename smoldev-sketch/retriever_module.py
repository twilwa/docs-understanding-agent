# Importing necessary libraries
from langchain.retrieval import RetrievalQaChain
from langchain.encoders import BM25Encoder
from pinecone import PineconeHybridSearchRetriever

# Function to initialize Retrievers
def create_retrievers(pinecone_db):
    # Initialize the retriever with the Pinecone database
    retriever = PineconeHybridSearchRetriever(database=pinecone_db, vector_dim=1024)
    # Use the BM25Encoder for the retriever
    retriever.encoder = BM25Encoder()
    
    # Initialize the RetrievalQaChains for documentation and repository respectively
    doc_retrieval_chain = RetrievalQaChain(retriever=retriever, name='doc_retrieval_chain')
    repo_retrieval_chain = RetrievalQaChain(retriever=retriever, name='repo_retrieval_chain')
    
    return doc_retrieval_chain, repo_retrieval_chain

# Expose the RetrievalQaChains for documentation and repository
doc_retrieval_chain, repo_retrieval_chain = create_retrievers(pinecone_db)
