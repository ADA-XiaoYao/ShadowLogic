from src.llm_agent import LLMAgent
import json

class RemediationHardeningAdvisor:
    """ShadowShield's Remediation & Hardening Advisor for mitigating identified vulnerabilities
    and hardening AI systems.
    """

    def __init__(self):
        self.agent = LLMAgent()

    def get_remediation_advice(self, vulnerability_details, model_type, deployment_context, context=None):
        """Provides actionable advice and automated scripts for mitigating identified vulnerabilities.

        Args:
            vulnerability_details (str): Detailed description of the identified vulnerability.
            model_type (str): Type of the AI model (e.g., LLM, image classifier).
            deployment_context (str): Description of the deployment environment (e.g., cloud, on-premise, specific framework).
            context (str, optional): Additional context about the system or existing security controls.

        Returns:
            str: Detailed remediation advice, including code examples and configuration changes.
        """
        context_str = f"Additional Context: {context}\n" if context else ""
        prompt = (
            f"As a top-tier AI security expert, provide detailed remediation advice for the following vulnerability.\n"
            f"Vulnerability Details: {vulnerability_details}\n"
            f"AI Model Type: {model_type}\n"
            f"Deployment Context: {deployment_context}\n"
            f"{context_str}"
            "Your advice should include:\n"
            "1. **Specific Mitigation Steps**: Step-by-step instructions to fix the vulnerability.\n"
            "2. **Code Examples/Configuration Changes**: Provide concrete code snippets or configuration adjustments where applicable.\n"
            "3. **Hardening Recommendations**: General recommendations to improve the overall security posture of the AI system.\n"
            "4. **Verification Steps**: How to verify that the remediation was successful.\n"
            "Present the advice in a clear, actionable, and technical format."
        )
        return self.agent.ask(prompt)

    def get_hardening_guidelines(self, model_type, deployment_context, security_goals=None, context=None):
        """Provides general hardening guidelines for AI systems.

        Args:
            model_type (str): Type of the AI model (e.g., LLM, image classifier).
            deployment_context (str): Description of the deployment environment.
            security_goals (list, optional): Specific security goals (e.g., data privacy, model integrity, availability).
            context (str, optional): Additional context about the system.

        Returns:
            str: Comprehensive hardening guidelines.
        """
        goals_str = f"Specific Security Goals: {json.dumps(security_goals)}\n" if security_goals else ""
        context_str = f"Additional Context: {context}\n" if context else ""
        prompt = (
            f"As a top-tier AI security expert, provide comprehensive hardening guidelines for the following AI system.\n"
            f"AI Model Type: {model_type}\n"
            f"Deployment Context: {deployment_context}\n"
            f"{goals_str}"
            f"{context_str}"
            "Your guidelines should cover:\n"
            "1. **Data Security**: Recommendations for protecting training and inference data.\n"
            "2. **Model Integrity**: Strategies to prevent model tampering and ensure trustworthiness.\n"
            "3. **Access Control**: Best practices for managing access to AI models and infrastructure.\n"
            "4. **Monitoring & Logging**: Recommendations for detecting and responding to security incidents.\n"
            "5. **Secure Development Lifecycle**: Advice for integrating security throughout the AI development process.\n"
            "Present the guidelines in a structured and actionable format."
        )
        return self.agent.ask(prompt)
