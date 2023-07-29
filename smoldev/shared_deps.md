Plan:

The application will be structured into several modules:

1. **Loader Module**: This module will be responsible for loading the documents from the sitemap and the Github repository. It will use a SitemapLoader and a WebBaseLoader, respectively, to accomplish this task. It will export a list of chunks, each associated with the metadata including source, url, title, and type.

2. **Embedding Module**: This module will use the OpenAI library to embed the chunks into vectors and store them in a Pinecone vector database. The dimension size of the vectors will be 1024. It exports the Pinecone database instance.

3. **Retriever Module**: This module will use the BM25Encoder to create a PineconeHybridSearchRetriever to retrieve information from the Pinecone database. It will export two RetrievalQaChains, one for the documentation and another for the repo.

4. **Agent Module**: This module will create a conversation agent that uses the RetrievalQaChains to provide relevant information based on the user's query. It will use a custom schema, `CustomResponseSchema`, which includes an answer field and a sources field. It exports the agent instance.

5. **Interface Module**: This module will use Streamlit to create a conversational app front end where the user can input their query and see the sources along with the agent's response. It exports the Streamlit app instance.

**Variables exported**:

- Loader Module: `chunks`
- Embedding Module: `pinecone_db`
- Retriever Module: `doc_retrieval_chain`, `repo_retrieval_chain`
- Agent Module: `agent`
- Interface Module: `app`

**Data schemas**:

- `CustomResponseSchema`: Includes `answer` and `sources` fields.

**DOM Element IDs**:

In the Interface Module, we'll have the following DOM elements:

- `user_query_input`: An input field where the user enters their query.
- `response_display`: A display area where the agent's response and the sources are shown.

**Message Names**:

For the purpose of this plan, assuming that "message names" refers to the names of messages exchanged between different parts of the application, we have:

- `query`: The user's query, sent from the Interface Module to the Agent Module.
- `response`: The response from the Agent, sent from the Agent Module to the Interface Module.

**Function Names**:

- Loader Module: `load_sitemap`, `load_repo`
- Embedding Module: `embed_chunks`
- Retriever Module: `create_retrievers`
- Agent Module: `create_agent`
- Interface Module: `create_interface`