# ShadowLogic AI

**ShadowLogic** 是一款基于大型语言模型 (LLM) 的先进命令行渗透测试辅助工具。它将 AI 的逻辑推理能力与渗透测试的实战需求相结合，为安全研究人员提供智能化的漏洞分析、Payload 生成和决策支持。

## 核心特性

- 🧠 **智能漏洞分析**：解析扫描结果，识别潜在攻击面，并提供深度的逻辑分析。
- 🧨 **定制 Payload 生成**：根据特定漏洞上下文，生成针对性的利用 Payload。
- 🔍 **扫描集成辅助**：支持 Nmap 等工具的输出分析，将其转化为可操作的攻击建议。
- 💬 **AI 渗透顾问**：随时通过命令行向 AI 咨询复杂的渗透测试问题。

## 快速开始

### 安装

1. 克隆仓库：
   ```bash
   git clone https://github.com/yourusername/shadowlogic.git
   cd shadowlogic
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 配置 API Key：
   在环境变量中设置 `OPENAI_API_KEY`。

### 使用示例

- **分析 Nmap 扫描结果**：
  ```bash
  python pentest_ai.py analyze -f nmap_scan.txt
  ```

- **生成 SQL 注入 Payload**：
  ```bash
  python pentest_ai.py payload "SQL Injection" --context "id parameter in login page"
  ```

- **咨询渗透建议**：
  ```bash
  python pentest_ai.py ask "如何绕过特定 WAF 的 XSS 检测？"
  ```

## 项目结构

```
shadowlogic/
├── README.md
├── requirements.txt
├── pentest_ai.py         # 程序入口
├── src/
│   ├── cli.py            # 命令行逻辑
│   ├── llm_agent.py      # AI 核心引擎
│   ├── modules/          # 功能模块
│   └── utils/            # 工具类
└── docs/                 # 项目文档
```

## 免责声明

本工具仅用于合法的授权渗透测试和安全研究。使用者需遵守相关法律法规，严禁用于非法攻击。作者对因滥用本工具导致的任何后果不承担责任。
