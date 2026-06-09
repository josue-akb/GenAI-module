from ollama import chat
from tools import TOOLS, TOOLS_SCHEMA


class Agent:
    def __init__(self, model: str = "llama3.2:3b", system_prompt: str = ""):
        self.model = model
        self.history = [
            {"role": "system", "content": system_prompt}
        ]
        self.max_iterations = 10

    def run(self, user_input: str) -> str:
        self.history.append({"role": "user", "content": user_input})

        for _ in range(self.max_iterations):

            response = chat(
                model=self.model,
                messages=self.history,
                tools=TOOLS_SCHEMA
            )

            msg = response["message"]
            self.history.append(msg)

            if not msg.get("tool_calls"):
                return msg["content"]

            for call in msg["tool_calls"]:
                result = self._execute_tool(call)

                self.history.append({
                    "role": "tool",
                    "content": str(result),
                    "tool_name": call["function"]["name"]
                })

        return "Limite d'itérations atteinte"

    def _execute_tool(self, call: dict):
        fn_name = call["function"]["name"]
        fn_args = call["function"]["arguments"]

        if fn_name not in TOOLS:
            return f"Erreur : outil inconnu {fn_name}"

        try:
            return TOOLS[fn_name](**fn_args)
        except Exception as e:
            return f"Erreur outil : {e}"