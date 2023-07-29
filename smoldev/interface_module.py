from pydantic import BaseModel, Field
from typing import List

class CustomResponseSchema(BaseModel):
    """An answer to the question being asked, with sources."""

    answer: str = Field(..., description="Answer to the question that was asked")
    sources: List[str] = Field(
        ..., description="List of sources used to answer the question"
    )


def create_interface():
    st.title('Langchain and OpenAI Chat Interface')
    
    user_query_input = st.text_input("Enter your query here")
    if st.button('Submit Query'):
        response = agent.handle_query(user_query_input)
        display_response(response)
        
def display_response(response):
    st.subheader('Response:')
    st.write(response['answer'])
    
    st.subheader('Sources:')
    for source in response['sources']:
        st.write(source)
        
if __name__ == "__main__":
    create_interface()
