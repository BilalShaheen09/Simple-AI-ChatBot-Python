class RunConfig:
    def __init__(self, model, model_provider, tracing_disabled=True):
        self.model = model
        self.model_provider = model_provider
        self.tracing_disabled = tracing_disabled
