from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Form
from apps.llm import AgentExecutor, agent, parser
from apps.tools import search_tool, wiki_tool
from apps.models import QueryRequest

load_dotenv()

app = FastAPI()


@app.post('/seek')
async def seek(request:QueryRequest):
    try:
        agent_executor = AgentExecutor(agent=agent, tools=[search_tool], verbose=True)
        query = request.query
        raw_response = agent_executor.invoke({"query": query})
        structured_response = parser.parse(raw_response.get("output")[0]["text"])
        return {"success": True, "response": structured_response}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error parsing response: {str(e)}"
        )