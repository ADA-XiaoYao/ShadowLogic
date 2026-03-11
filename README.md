# ShadowLogic AI

**ShadowLogic** is an advanced command-line penetration testing assistant tool powered by Large Language Models (LLM). It combines the logical reasoning capabilities of AI with the practical demands of penetration testing, providing security researchers with intelligent vulnerability analysis, payload generation, and decision support.

## Key Features

- 🧠 **Intelligent Vulnerability Analysis**: Parses scan results, identifies potential attack surfaces, and provides in-depth logical analysis.
- 🧨 **Custom Payload Generation**: Generates targeted exploitation payloads based on specific vulnerability contexts.
- 🔍 **Scanner Integration Assistance**: Supports analysis of outputs from tools like Nmap, transforming them into actionable attack recommendations.
- 💬 **AI Penetration Consultant**: Ask complex penetration testing questions to the AI directly from the command line.

## Quick Start

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ADA-XiaoYao/ShadowLogic.git
   cd ShadowLogic
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure API Key:
   Set your `OPENAI_API_KEY` as an environment variable.

### Usage Examples

- **Analyze Nmap scan results**:
  ```bash
  python shadowlogic.py analyze -f nmap_scan.txt
  ```

- **Generate SQL Injection Payload**:
  ```bash
  python shadowlogic.py payload "SQL Injection" --context "id parameter in login page"
  ```

- **Consult for penetration advice**:
  ```bash
  python shadowlogic.py ask "How to bypass XSS detection of a specific WAF?"
  ```

## Project Structure

```
shadowlogic/
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── shadowlogic.py        # Main entry point
├── src/
│   ├── __init__.py
│   ├── cli.py            # Command-line interface logic
│   ├── llm_agent.py      # AI core engine
│   ├── modules/          # Functional modules
│   └── utils/            # Utility classes
└── docs/                 # Project documentation
```

## Disclaimer

This tool is intended for legitimate and authorized penetration testing and security research only. Users must comply with relevant laws and regulations, and any illegal attacks are strictly prohibited. The author is not responsible for any consequences resulting from the misuse of this tool.
