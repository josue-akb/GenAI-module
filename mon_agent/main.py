from agent import Agent
from prompts import SYSTEM_PROMPT


agent = Agent(
    model="llama3.2:3b",
    system_prompt=SYSTEM_PROMPT
)

while True:
    user_input = input("\n> ")

    if user_input.lower() in ["exit", "quit"]:
        break

    response = agent.run(user_input)
    print("\n", response)