from src.llm_agent import LLMAgent
import datetime

class ReportGenerator:
    """ShadowLogic 的报告生成模块。"""
    
    def __init__(self):
        self.agent = LLMAgent()

    def generate_markdown_report(self, target, vulnerabilities, summary):
        """生成 Markdown 格式的渗透测试报告。"""
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        
        prompt = (
            f"请为目标 {target} 生成一份结构化的渗透测试报告（Markdown 格式）。\n"
            f"测试日期: {date}\n"
            f"发现的漏洞列表: {vulnerabilities}\n"
            f"测试总结: {summary}\n\n"
            "报告应包含：1. 执行摘要, 2. 漏洞详情（描述、影响、修复建议）, 3. 总体安全建议。"
        )
        
        report_content = self.agent.ask(prompt)
        
        # 将报告保存到本地
        report_filename = f"report_{target}_{date}.md".replace("/", "_")
        with open(report_filename, 'w') as f:
            f.write(report_content)
            
        return f"报告已生成并保存至: {report_filename}"
