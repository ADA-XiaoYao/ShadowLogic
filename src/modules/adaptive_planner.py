from src.llm_agent import LLMAgent

class AdaptivePlanner:
    """ShadowLogic's Adaptive Planning Module for dynamic attack strategy adjustment."""
    
    def __init__(self):
        self.agent = LLMAgent()

    def adapt_strategy(self, current_situation, previous_actions, feedback, context=None):
        """Adapts the attack strategy based on real-time feedback and environmental changes.
        
        Args:
            current_situation (str): Description of the current state of the penetration test.
            previous_actions (str): A summary of actions taken so far.
            feedback (str): Feedback received from the target system or tools.
            context (str, optional): Additional context information. Defaults to None.
            
        Returns:
            str: An updated attack plan or adjusted strategy.
        """
        prompt = (
            f"As a top-tier red team operator, analyze the following information to adapt the current attack strategy.\n"
            f"Current Situation: {current_situation}\n"
            f"Previous Actions: {previous_actions}\n"
            f"Feedback Received: {feedback}\n"
        )
        if context:
            prompt += f"Additional Context: {context}\n"
        prompt += (
            "Based on this, provide an updated attack plan or adjusted strategy. "
            "Consider alternative approaches, new opportunities, and ways to overcome obstacles. "
            "Focus on achieving the objective efficiently and stealthily."
        )
        return self.agent.ask(prompt)
