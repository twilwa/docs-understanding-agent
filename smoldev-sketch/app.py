# Importing necessary libraries and modules
import streamlit as st
from langchain import SitemapLoader, WebBaseLoader, BM25Encoder, RetrievalQaChain
from pinecone import Pinecone
from openai import OpenAI
from pydantic import BaseModel, Field
from typing import List

# Custom schema for agent's responses
class CustomResponseSchema(BaseModel):
    """An answer to the question being asked, with sources."""
    answer: str = Field(..., description="Answer to the question that was asked")
    sources: List[str] = Field(
        ..., description="List of sources used to answer the question"
    )

# Loader for the sitemap documents
sitemap_loader = SitemapLoader()

# Loader for the Github repository documents
repo_loader = WebBaseLoader()

# OpenAI library instance
openai = OpenAI()

# Pinecone instance
pinecone = Pinecone()

# BM25 Encoder instance
bm25_encoder = BM25Encoder()

# Creating a Pinecone Hybrid Search Retriever for documentation
doc_retriever = PineconeHybridSearchRetreiver(pinecone, bm25_encoder)

# Creating a Pinecone Hybrid Search Retriever for repository
repo_retriever = PineconeHybridSearchRetreiver(pinecone, bm25_encoder)

# Retrieval Qa Chains for documentation and repository
doc_retrieval_chain = RetrievalQaChain(doc_retriever)
repo_retrieval_chain = RetrievalQaChain(repo_retriever)

# Conversation agent
agent = ConversationAgent(doc_retrieval_chain, repo_retrieval_chain)

# Streamlit application front-end
def app():
    st.title("Conversational Agent Interface")
    user_query = st.text_input("Please enter your query", id='user_query_input')
    if st.button("Submit"):
        response = agent.query(user_query)
        st.write(response.answer, id='response_display')
        for source in response.sources:
            st.write(source)

if __name__ == "__main__":
    app()
