from src.llm_agent import LLMAgent

class AttackGraphAnalyzer:
    """ShadowLogic's Attack Graph Analysis Module for identifying optimal attack paths."""
    
    def __init__(self):
        self.agent = LLMAgent()

    def analyze_graph(self, vulnerabilities, assets, network_topology, context=None):
        """Analyzes potential attack paths based on vulnerabilities, assets, and network topology.
        
        Args:
            vulnerabilities (str): A description of discovered vulnerabilities.
            assets (str): A description of target assets.
            network_topology (str): A description of the network topology.
            context (str, optional): Additional context information. Defaults to None.
            
        Returns:
            str: Analysis of optimal attack paths and recommendations.
        """
        prompt = (
            f"As a top-tier red team operator, analyze the following information to construct and analyze an attack graph.\n"
            f"Discovered Vulnerabilities: {vulnerabilities}\n"
            f"Target Assets: {assets}\n"
            f"Network Topology: {network_topology}\n"
        )
        if context:
            prompt += f"Additional Context: {context}\n"
        prompt += (
            "Identify optimal attack paths, critical choke points, and potential high-impact exploitation sequences. "
            "Provide a detailed explanation of the attack flow and recommendations for defensive measures or further offensive actions."
        )
        return self.agent.ask(prompt)
