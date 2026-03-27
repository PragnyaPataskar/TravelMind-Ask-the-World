from langchain_classic.agents import initialize_agent, AgentType
from src.llm.llm_handler import get_llm
from src.agents.tools import tools

SYSTEM_PROMPT = """
You are a smart travel assistant.

Always return responses in JSON format:

{{
  "city": "name",
  "weather": {{}},
  "air_quality": {{}},
  "places": ["place1", "place2"],
  "summary": "final answer"
}}

Use tools when needed.
"""

def get_agent():
    llm = get_llm()

    agent = initialize_agent(
      tools,
      llm,
      agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
      verbose=True,
      handle_parsing_errors=True,
      agent_kwargs={"system_message": SYSTEM_PROMPT}
    )

    return agent