from sitemap_loader import SitemapLoader
from document_chunker import DocumentChunker
from pinecone_database import PineconeDatabase
from web_base_loader import WebBaseLoader
from bm25_encoder import BM25Encoder
from retreival_qa import RetreivalQA
from conversation_agent import ConversationAgent
from custom_response_schema import CustomResponseSchema
from streamlit_app import StreamlitApp

def main():
    # Load all pages from a provided sitemap link
    sitemap_loader = SitemapLoader("sitemap_link")
    pages = sitemap_loader.load_sitemap()

    # Chunk the documents and embed them into vectors
    document_chunker = DocumentChunker()
    vectors = document_chunker.chunk_and_embed(pages)

    # Store vectors in a Pinecone vector database
    pinecone_database = PineconeDatabase()
    pinecone_database.store_vectors(vectors)

    # Load documents from a provided GitHub repo
    web_base_loader = WebBaseLoader("repo_url")
    documents = web_base_loader.load_documents()

    # Create a PineconeHybridSearchRetriever
    bm25_encoder = BM25Encoder()
    retriever = bm25_encoder.create_retriever()

    # Create a langchain retrievalqachain for each retriever type
    retreival_qa = RetreivalQA()
    qa_chain = retreival_qa.create_chain(retriever)

    # Provide relevant information based on the user's query
    conversation_agent = ConversationAgent()
    response = conversation_agent.get_response("user_query")

    # Define the custom schema for the agent's responses
    custom_response_schema = CustomResponseSchema()
    schema = custom_response_schema.define_schema()

    # Create a Streamlit conversational app frontend for user interaction
    streamlit_app = StreamlitApp()
    streamlit_app.run()

if __name__ == "__main__":
    main()
