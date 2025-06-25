"""LLM agent routing module."""


class AgentRouter:
    """Simple interface to query an LLM provider."""

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key

    def query_llm(self, prompt: str) -> str:
        """Send prompt to LLM and return response.

        This is a placeholder implementation. Integrate OpenAI or other
        provider here.
        """
        # TODO: Add real API call to OpenAI or local model
        return "LLM response placeholder"
