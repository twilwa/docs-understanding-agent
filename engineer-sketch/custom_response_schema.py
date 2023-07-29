from pydantic import BaseModel, Field

class CustomResponseSchema(BaseModel):
    def define_schema(self):
        # Code to define the custom schema for the agent's responses
        pass
