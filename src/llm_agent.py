import os
from openai import OpenAI

class LLMAgent:
    """ShadowLogic's core LLM interaction agent."""
    
    def __init__(self, model="gpt-4.1-mini"):
        # Use pre-configured OpenAI client
        self.client = OpenAI()
        self.model = model
        self.system_prompt = (
            "You are an international top-tier penetration testing expert and AI assistant, named ShadowLogic."
            "Your task is to assist penetration testers with vulnerability analysis, payload generation, scan result interpretation, attack path planning, and report writing."
            "Your responses must have the following characteristics:\n"
            "1. **Professionalism**: Use precise penetration testing terminology and concepts.\n"
            "2. **Rigor**: Provide analysis based on facts and logic, avoiding speculation.\n"
            "3. **Practicality**: Offer actionable, specific advice and payloads.\n"
            "4. **Security**: When providing any offensive information (e.g., payloads), you must include detailed usage instructions, potential risk warnings, and a statement of legality. Emphasize that it is for authorized testing only.\n"
            "5. **Structure**: For complex analyses, present information clearly using bullet points, paragraphs, or tables.\n"
            "6. **Ethical Guidelines**: Always adhere to cybersecurity ethics, refusing to provide advice for any illegal or malicious attacks.\n"
            "When performing vulnerability analysis, use a Chain-of-Thought (CoT) reasoning process to gradually analyze the problem and explain the inference steps.\n"
            "When generating payloads, consider the target environment, vulnerability type, and bypass mechanisms, and provide multiple variants.\n"
            "When users seek advice, offer multi-faceted solutions and evaluate their pros and cons."
        )

    def ask(self, prompt, user_context=None):
        """Directly ask the AI penetration testing related questions."""
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": prompt}
        ]
        
        if user_context:
            messages.insert(1, {"role": "system", "content": f"Context information: {user_context}"})
            
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error calling LLM: {str(e)}"

    def generate_payload(self, vuln_type, context=None):
        """Generates payloads for a specific vulnerability."""
        prompt = f"Please generate penetration testing payloads for the following vulnerability type: {vuln_type}."
        if context:
            prompt += f"\nContext information: {context}"
        prompt += "\nPlease provide at least 3 different payload variants, explaining their applicable scenarios and bypass principles."
        return self.ask(prompt)

    def analyze_data(self, data, data_type="scan_result"):
        """Analyzes scan results or target data."""
        prompt = (
            f"As a top-tier penetration testing expert, please analyze the following {data_type} using a Chain-of-Thought reasoning process.\n"
            f"The analysis should include:\n"
            f"1. Identify potential vulnerabilities and risks.\n"
            f"2. Assess the severity and impact of the vulnerabilities.\n"
            f"3. Provide detailed penetration testing recommendations and next steps.\n"
            f"4. Outline possible attack paths.\n\n{data}"
        )
        return self.ask(prompt)
