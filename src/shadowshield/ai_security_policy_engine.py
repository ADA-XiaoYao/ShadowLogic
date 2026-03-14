from src.llm_agent import LLMAgent
import json

class AISecurityPolicyEngine:
    """ShadowShield's AI Security Policy Engine for evaluating AI models and deployments
    against established security policies and best practices.
    """

    def __init__(self):
        self.agent = LLMAgent()

    def evaluate_policy_compliance(self, model_description, deployment_environment_description, policy_standards=None, context=None):
        """Evaluates AI models and deployments against established security policies and best practices.

        Args:
            model_description (str): Description of the AI model (e.g., its purpose, data used, algorithms).
            deployment_environment_description (str): Description of the deployment environment (e.g., cloud provider, security controls).
            policy_standards (list, optional): List of specific policy standards or best practices to check against (e.g., OWASP Top 10 for LLMs, NIST AI RMF).
            context (str, optional): Additional context about the organization's security posture or specific concerns.

        Returns:
            str: A compliance report detailing adherence to policies and identified gaps.
        """
        standards_str = f"Specific policy standards to check: {json.dumps(policy_standards)}\n" if policy_standards else ""
        context_str = f"Additional Context: {context}\n" if context else ""
        prompt = (
            f"As a top-tier AI security policy auditor, evaluate the following AI model and its deployment for compliance with security policies and best practices.\n"
            f"AI Model Description: {model_description}\n"
            f"Deployment Environment Description: {deployment_environment_description}\n"
            f"{standards_str}"
            f"{context_str}"
            "Generate a comprehensive compliance report. For each policy standard, indicate compliance status (Compliant, Partially Compliant, Non-Compliant) and provide detailed justifications. "
            "Identify any gaps, potential risks, and suggest high-level recommendations for improvement.\n"
            "If no specific policy standards are provided, use general AI security best practices (e.g., data privacy, model integrity, responsible AI principles) for evaluation."
        )
        return self.agent.ask(prompt)
