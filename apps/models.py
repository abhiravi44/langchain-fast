from pydantic import BaseModel



class QueryRequest(BaseModel):
    query: str

    
class ResearchResponse(BaseModel):
    """the response model format the llm returns"""
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]