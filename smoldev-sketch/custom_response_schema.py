from pydantic import BaseModel, Field

class CustomResponseSchema(BaseModel):
    """A class used to represent the response schema for the conversation agent"""
    
    answer: str = Field(..., description="Answer to the question that was asked")
    sources: List[str] = Field(
        ..., description="List of sources used to answer the question"
    )
