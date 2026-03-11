from src.llm_agent import LLMAgent

class PayloadGenerator:
    """ShadowLogic's Payload Generation Module."""
    
    def __init__(self):
        self.agent = LLMAgent()

    def generate(self, vulnerability_type, context=None):
        """Generates payloads based on vulnerability type and context."""
        return self.agent.generate_payload(vulnerability_type, context)
