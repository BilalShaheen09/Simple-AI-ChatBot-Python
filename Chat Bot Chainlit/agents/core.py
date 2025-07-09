class Agent:
    def __init__(self, name, instructions, model):
        self.name = name
        self.instructions = instructions
        self.model = model

class Runner:
    @staticmethod
    def run_sync(starting_agent, input, run_config):
        class Result:
            final_output = f"Simulated response to: {input[-1]['content']}"
            def to_input_list(self):
                return input
        return Result()

class AsyncOpenAI:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url

class OpenAIChatCompletionsModel:
    def __init__(self, model, openai_client):
        self.model = model
        self.openai_client = openai_client
