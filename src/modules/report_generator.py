from src.llm_agent import LLMAgent
import datetime
import os

class ReportGenerator:
    """ShadowLogic's report generation module."""
    
    def __init__(self):
        self.agent = LLMAgent()

    def generate_markdown_report(self, target, vulnerabilities, summary):
        """Generates a Markdown-formatted penetration test report."""
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        prompt = (
            f"Please generate a structured penetration test report (in Markdown format) for the target {target}.\n"
            f"Test Date: {date}\n"
            f"Discovered Vulnerabilities: {vulnerabilities}\n"
            f"Test Summary: {summary}\n\n"
            "The report should include: 1. Executive Summary, 2. Vulnerability Details (description, impact, remediation suggestions), 3. Overall Security Recommendations."
        )
        
        report_content = self.agent.ask(prompt)
        
        # Save the report locally
        report_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "reports")
        if not os.path.exists(report_dir):
            os.makedirs(report_dir)
        report_filename = os.path.join(report_dir, f"report_{target}_{date}.md".replace("/", "_"))
        with open(report_filename, 'w') as f:
            f.write(report_content)
            
        return f"Report generated and saved to: {report_filename}"
