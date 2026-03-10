from src.llm_agent import LLMAgent

class PayloadGenerator:
    """ShadowLogic 的 Payload 生成模块。"""
    
    def __init__(self):
        self.agent = LLMAgent()

    def generate(self, vulnerability_type, context=None):
        """根据漏洞类型和上下文生成 Payload。"""
        return self.agent.generate_payload(vulnerability_type, context)
