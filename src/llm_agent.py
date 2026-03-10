import os
from openai import OpenAI

class LLMAgent:
    """ShadowLogic 的核心 LLM 交互代理。"""
    
    def __init__(self, model="gpt-4.1-mini"):
        # 使用预配置的 OpenAI 客户端
        self.client = OpenAI()
        self.model = model
        self.system_prompt = (
            "你是一个专业的渗透测试人工智能助手，名为 ShadowLogic。"
            "你的任务是协助渗透测试人员进行漏洞分析、Payload 生成、扫描结果解读等。"
            "你的回答必须专业、严谨，并始终遵循网络安全伦理准则。"
            "在提供 Payload 时，请务必附带详细的使用说明和安全警示。"
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
        return self.ask(prompt)

    def analyze_data(self, data, data_type="scan_result"):
        """分析扫描结果或目标数据。"""
        prompt = f"请分析以下{data_type}，识别潜在的漏洞点并给出渗透建议:\n\n{data}"
        return self.ask(prompt)
