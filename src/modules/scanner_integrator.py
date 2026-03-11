import re
from src.llm_agent import LLMAgent

class ScannerIntegrator:
    """ShadowLogic's scanner integration module, responsible for parsing output from various scanning tools."""
    
    def __init__(self):
        self.agent = LLMAgent()

    def parse_nmap(self, nmap_output):
        """Parses Nmap scan results and generates an analysis."""
        # Simple regex to extract open ports and services to construct a more refined Prompt
        open_ports = re.findall(r"(\d+/tcp\s+open\s+\S+)", nmap_output)
        summary = "\n".join(open_ports)
        
        prompt = (
            f"As a top-tier penetration testing expert, analyze the following open ports and services discovered by Nmap scan:\n{summary}\n\n"
            "Based on this information, identify high-risk services and provide targeted penetration testing recommendations, potential attack path analysis, and risk level assessment."
        )
        return self.agent.ask(prompt)

    def parse_zap(self, zap_output):
        """Parses OWASP ZAP scan results and generates an analysis."""
        prompt = (
            f"As a top-tier penetration testing expert, analyze the following vulnerability information discovered by OWASP ZAP scan:\n\n{zap_output}\n\n"
            "Based on this information, identify critical vulnerabilities and provide detailed remediation suggestions, impact assessment, and further manual testing recommendations."
        )
        return self.agent.ask(prompt)

    def parse_generic(self, tool_name, output):
        """Generic parser."""
        prompt = f"The following is the scan output from tool {tool_name}. Please analyze the potential security risks within:\n\n{output}"
        return self.agent.ask(prompt)
