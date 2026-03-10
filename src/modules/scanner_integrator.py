import re
from src.llm_agent import LLMAgent

class ScannerIntegrator:
    """ShadowLogic 的扫描器集成模块，负责解析各种扫描工具的输出。"""
    
    def __init__(self):
        self.agent = LLMAgent()

    def parse_nmap(self, nmap_output):
        """解析 Nmap 扫描结果并生成分析。"""
        # 简单的正则提取开放端口和服务，以便构建更精炼的 Prompt
        open_ports = re.findall(r"(\d+/tcp\s+open\s+\S+)", nmap_output)
        summary = "\n".join(open_ports)
        
        prompt = (
            f"请作为一名顶级渗透测试专家，分析以下 Nmap 扫描发现的开放端口和服务：\n{summary}\n\n"
            "请根据这些信息，识别高风险服务，并提供针对性的渗透测试建议、潜在攻击路径分析及风险等级评估。"
        )
        return self.agent.ask(prompt)

    def parse_zap(self, zap_output):
        """解析 OWASP ZAP 扫描结果并生成分析。"""
        prompt = (
            f"请作为一名顶级渗透测试专家，分析以下 OWASP ZAP 扫描发现的漏洞信息：\n\n{zap_output}\n\n"
            "请根据这些信息，识别关键漏洞，并提供详细的修复建议、影响评估及进一步的手工测试建议。"
        )
        return self.agent.ask(prompt)

    def parse_generic(self, tool_name, output):
        """通用解析器。"""
        prompt = f"以下是工具 {tool_name} 的扫描输出，请分析其中的潜在安全风险：\n\n{output}"
        return self.agent.ask(prompt)
