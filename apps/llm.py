from dotenv import load_dotenv
from langchain_openai import OpenAI as LLMOpenAI
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from .template import parser, prompt

# Language model for LangChain
# llm = LLMOpenAI(temperature=0.7, max_tokens=500, streaming=True, batch_size=50)

load_dotenv()

llm = ChatOpenAI(model='gpt-4o-mini')
# llm2 = ChatAnthropic(model_name='claude-3-5-sonet-20241022')

# response = llm.invoke("What is the meaning of life?")
# print(response)

# tools = [search_tool, wiki_tool, save_tool]
tools = []
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)
