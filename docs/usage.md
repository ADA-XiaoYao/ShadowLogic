# ShadowLogic 使用指南

**ShadowLogic** 是一款基于 AI 的命令行渗透测试辅助工具，旨在帮助安全研究人员更高效地进行漏洞分析、Payload 生成和报告撰写。

## 安装

1.  **克隆仓库**：
    ```bash
    git clone https://github.com/yourusername/shadowlogic.git
    cd shadowlogic
    ```

2.  **安装依赖**：
    ```bash
    pip install -r requirements.txt
    ```

3.  **配置 API Key**：
    ShadowLogic 依赖大型语言模型（LLM）提供智能服务。您需要设置相应的 API Key。目前支持 OpenAI API，请将您的 OpenAI API Key 设置为环境变量 `OPENAI_API_KEY`。

    **Linux/macOS**：
    ```bash
    export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

    **Windows (Command Prompt)**：
    ```bash
    set OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

    **Windows (PowerShell)**：
    ```powershell
    $env:OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

## 命令概览

ShadowLogic 提供以下主要命令：

*   `shadowlogic analyze`：分析目标或扫描结果中的潜在漏洞。
*   `shadowlogic payload`：根据漏洞类型和上下文生成 Payload。
*   `shadowlogic ask`：直接向 AI 提问渗透测试相关问题。
*   `shadowlogic report`：根据发现的漏洞生成渗透测试报告。
*   `shadowlogic parse`：解析扫描工具的输出并提供分析建议。

## 详细使用说明

### 1. `analyze` - 漏洞分析

此命令用于分析特定的渗透测试目标或已有的扫描结果文件，以识别潜在的漏洞和攻击面。

**用法**：

```bash
shadowlogic analyze [--target <目标>] [--input-file <文件路径>]
```

**参数**：

*   `-t, --target <目标>`：指定要分析的目标，可以是 IP 地址、域名等。
*   `-f, --input-file <文件路径>`：指定包含扫描结果的文件路径（例如 Nmap 输出）。

**示例**：

*   分析特定目标：
    ```bash
    shadowlogic analyze -t example.com
    ```

*   分析 Nmap 扫描结果文件：
    ```bash
    shadowlogic analyze -f nmap_scan_results.txt
    ```

### 2. `payload` - Payload 生成

此命令根据指定的漏洞类型和上下文信息，生成定制化的攻击 Payload。

**用法**：

```bash
shadowlogic payload <漏洞类型> [--context <上下文信息>]
```

**参数**：

*   `<漏洞类型>`：必填，指定要生成 Payload 的漏洞类型（例如 
