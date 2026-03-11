from src.llm_agent import LLMAgent
import subprocess
import json

class ReconnaissanceModule:
    """ShadowLogic's Reconnaissance Module for passive and active information gathering."""
    
    def __init__(self):
        self.agent = LLMAgent()

    def passive_recon(self, target):
        """Performs passive reconnaissance on a given target using OSINT techniques."""
        prompt = (
            f"As a top-tier red team operator, conduct passive reconnaissance for the target: {target}.\n"
            "Focus on gathering Open-Source Intelligence (OSINT) without direct interaction with the target.\n"
            "Information to collect includes:\n"
            "- Domain registration details (WHOIS)\n"
            "- Subdomains and associated IP addresses\n"
            "- Publicly exposed email addresses and employee names\n"
            "- Social media presence\n"
            "- Related public documents or data leaks\n"
            "- Technologies used (from public sources like Wappalyzer data if available)\n"
            "Provide a structured report of your findings, highlighting any potentially valuable information for further attack planning."
        )
        return self.agent.ask(prompt)

    def active_recon(self, target):
        """Performs active reconnaissance on a given target using tools like Nmap (simulated)."""
        # In a real scenario, this would execute Nmap and parse its output.
        # For now, we'll simulate Nmap output and ask the LLM to analyze it.
        simulated_nmap_output = f"""
Nmap scan report for {target} (192.168.1.1)
Host is up (0.0010s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
443/tcp  open  https
3306/tcp open  mysql

Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds
"""
        prompt = (
            f"As a top-tier red team operator, analyze the following simulated Nmap scan results for the target {target}:\n\n{simulated_nmap_output}\n\n"
            "Identify open ports, services, and potential vulnerabilities. Provide recommendations for further active reconnaissance or initial access attempts, considering common attack vectors for these services."
        )
        return self.agent.ask(prompt)

    def enumerate_subdomains(self, domain):
        """Enumerates subdomains for a given domain (simulated)."""
        # In a real scenario, this would use tools like Sublist3r, Amass, or Ffuf.
        simulated_subdomains = [
            f"www.{domain}",
            f"mail.{domain}",
            f"dev.{domain}",
            f"admin.{domain}"
        ]
        prompt = (
            f"As a top-tier red team operator, analyze the following simulated subdomain enumeration results for {domain}:\n\n{', '.join(simulated_subdomains)}\n\n"
            "Identify any interesting subdomains that might host different applications or services, and suggest further investigation steps for each."
        )
        return self.agent.ask(prompt)
