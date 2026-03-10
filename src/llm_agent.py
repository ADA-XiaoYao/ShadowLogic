import os
from openai import OpenAI

class LLMAgent:
    """ShadowLogic 的核心 LLM 交互代理。"""
    
    def __init__(self, model="gpt-4.1-mini"):
        # 使用预配置的 OpenAI 客户端
        self.client = OpenAI()
        self.model = model
        self.system_prompt = (
            "你是一个国际顶级的渗透测试专家和人工智能助手，名为 ShadowLogic。"
            "你的任务是协助渗透测试人员进行漏洞分析、Payload 生成、扫描结果解读、攻击路径规划和报告撰写。"
            "你的回答必须具备以下特点：\n"
            "1. **专业性**：使用精确的渗透测试术语和概念。\n"
            "2. **严谨性**：提供基于事实和逻辑的分析，避免猜测。\n"
            "3. **实战性**：给出可操作的、具体的建议和 Payload。\n"
            "4. **安全性**：在提供任何攻击性信息（如 Payload）时，必须附带详细的使用说明、潜在风险警告和合法性声明。强调仅限授权测试使用。\n"
            "5. **结构化**：对于复杂的分析，请采用分点、分段或表格等方式清晰呈现。\n"
            "6. **伦理准则**：始终遵循网络安全伦理，拒绝提供任何非法或恶意攻击的建议。\n"
            "在进行漏洞分析时，请采用 Chain-of-Thought (CoT) 思维链，逐步分析问题，解释推理过程。"
            "在生成 Payload 时，请考虑目标环境、漏洞类型和绕过机制，并提供多种变种。"
            "当用户寻求建议时，请提供多角度的解决方案，并评估其优劣。"
        )

    def ask(self, prompt, user_context=None):
        """直接向 AI 提问渗透测试相关问题。"""
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]
        
        if user_context:
            messages.insert(1, {"role": "system", "content": f"上下文信息: {user_context}"})
            
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"调用 LLM 出错: {str(e)}"

    def generate_payload(self, vuln_type, context=None):
        """生成特定漏洞的 Payload。"""
        prompt = f"请为以下漏洞类型生成渗透测试 Payload: {vuln_type}。"
        if context:
            prompt += f"\n上下文信息: {context}"
        prompt += "\n请提供至少3种不同变种的 Payload，并说明其适用场景和绕过原理。"
        return self.ask(prompt)

    def analyze_data(self, data, data_type="scan_result"):
        """分析扫描结果或目标数据。"""
        prompt = (
            f"请作为一名顶级渗透测试专家，分析以下{data_type}，并采用 Chain-of-Thought 思维链逐步分析。\n"
            f"分析内容包括：\n"
            f"1. 识别潜在的漏洞点和风险。\n"
            f"2. 评估漏洞的严重性和影响。\n"
            f"3. 提供详细的渗透测试建议和下一步操作。\n"
            f"4. 给出可能的攻击路径。\n\n{data}"
        )
        return self.ask(prompt)
