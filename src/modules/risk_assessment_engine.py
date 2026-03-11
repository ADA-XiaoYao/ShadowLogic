from src.llm_agent import LLMAgent

class RiskAssessmentEngine:
    """ShadowLogic's Risk Assessment Engine for dynamically assessing the risk of identified vulnerabilities and attack paths."""
    
    def __init__(self):
        self.agent = LLMAgent()

    def assess_risk(self, vulnerability_details, attack_path_info, context=None):
        """Dynamically assesses the risk of identified vulnerabilities and potential attack paths.
        
        Args:
            vulnerability_details (str): A description of discovered vulnerabilities.
            attack_path_info (str): Information about the identified attack paths.
            context (str, optional): Additional context information. Defaults to None.
            
        Returns:
            str: A detailed risk assessment, including severity, impact, and likelihood.
        """
        prompt = (
            f"As a top-tier red team operator and security analyst, perform a detailed risk assessment based on the following information.\n"
            f"Vulnerability Details: {vulnerability_details}\n"
            f"Attack Path Information: {attack_path_info}\n"
        )
        if context:
            prompt += f"Additional Context: {context}\n"
        prompt += (
            "Your assessment should include:\n"
            "1. **Severity Rating**: Assign a severity (e.g., Critical, High, Medium, Low) and justify it.\n"
            "2. **Potential Impact**: Describe the business and technical impact if the vulnerabilities are exploited via the identified attack paths.\n"
            "3. **Likelihood**: Estimate the likelihood of successful exploitation, considering attacker capabilities and existing controls.\n"
            "4. **Mitigation Recommendations**: Provide high-level recommendations to mitigate the identified risks.\n"
            "Present the assessment in a clear, structured format, suitable for a security report."
        )
        return self.agent.ask(prompt)
