# ShadowLogic User Guide

**ShadowLogic** is an AI-powered command-line penetration testing assistant tool designed to help security researchers conduct vulnerability analysis, payload generation, and report writing more efficiently.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/ADA-XiaoYao/ShadowLogic.git
    cd ShadowLogic
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key**:
    ShadowLogic relies on Large Language Models (LLM) for intelligent services. You need to set up the corresponding API Key. Currently, OpenAI API is supported; please set your OpenAI API Key as the environment variable `OPENAI_API_KEY`.

    **Linux/macOS**:
    ```bash
    export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

    **Windows (Command Prompt)**:
    ```bash
    set OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

    **Windows (PowerShell)**:
    ```powershell
    $env:OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
    ```

## Command Overview

ShadowLogic provides the following main commands:

*   `shadowlogic analyze`: Analyzes potential vulnerabilities in a target or scan results.
*   `shadowlogic payload`: Generates payloads based on vulnerability type and context.
*   `shadowlogic ask`: Directly asks the AI penetration testing related questions.
*   `shadowlogic report`: Generates a penetration test report based on discovered vulnerabilities.
*   `shadowlogic parse`: Parses scanner tool output and provides analysis recommendations.

## Detailed Usage

### 1. `analyze` - Vulnerability Analysis

This command is used to analyze specific penetration test targets or existing scan result files to identify potential vulnerabilities and attack surfaces.

**Usage**:

```bash
shadowlogic analyze [--target <target>] [--input-file <file_path>]
```

**Parameters**:

*   `-t, --target <target>`: Specifies the target to analyze, which can be an IP address, domain name, etc.
*   `-f, --input-file <file_path>`: Specifies the path to a file containing scan results (e.g., Nmap output).

**Examples**:

*   Analyze a specific target:
    ```bash
    shadowlogic analyze -t example.com
    ```

*   Analyze an Nmap scan result file:
    ```bash
    shadowlogic analyze -f nmap_scan_results.txt
    ```

### 2. `payload` - Payload Generation

This command generates customized attack payloads based on the specified vulnerability type and context information.

**Usage**:

```bash
shadowlogic payload <vulnerability_type> [--context <context_information>]
```

**Parameters**:

*   `<vulnerability_type>`: Required, specifies the type of vulnerability for which to generate a payload (e.g., "SQL Injection", "XSS").
*   `--context <context_information>`: Optional, provides additional context for payload generation, such as parameter names, injection points, or specific bypass techniques.

**Examples**:

*   Generate a basic SQL Injection payload:
    ```bash
    shadowlogic payload "SQL Injection" --context "login form username field"
    ```

*   Generate an XSS payload for a reflected XSS vulnerability:
    ```bash
    shadowlogic payload "Reflected XSS" --context "search query parameter"
    ```

### 3. `ask` - AI Penetration Consultant

This command allows you to directly ask the ShadowLogic AI any penetration testing related questions.

**Usage**:

```bash
shadowlogic ask "<your_question>"
```

**Parameters**:

*   `<your_question>`: Required, the question you want to ask the AI.

**Examples**:

*   Ask for advice on WAF bypass techniques:
    ```bash
    shadowlogic ask "What are some effective techniques to bypass a WAF for SQL Injection?"
    ```

*   Inquire about common misconfigurations in cloud environments:
    ```bash
    shadowlogic ask "What are the most common security misconfigurations in AWS S3 buckets?"
    ```

### 4. `report` - Report Generation

This command generates a structured penetration test report in Markdown format based on the discovered vulnerabilities and a summary of the test.

**Usage**:

```bash
shadowlogic report --target <target> --vulnerabilities <vulnerabilities> --summary <summary>
```

**Parameters**:

*   `-t, --target <target>`: Required, the target of the penetration test.
*   `-v, --vulnerabilities <vulnerabilities>`: Required, a comma-separated list of discovered vulnerabilities (e.g., "SQL Injection, XSS, RCE").
*   `-s, --summary <summary>`: Required, a brief summary of the penetration test findings.

**Examples**:

*   Generate a report for a web application:
    ```bash
    shadowlogic report -t webapp.com -v "SQL Injection, Broken Authentication" -s "Identified critical SQLi and authentication bypass vulnerabilities."
    ```

### 5. `parse` - Scanner Output Parsing

This command parses the output from various security scanning tools and provides an AI-driven analysis and recommendations.

**Usage**:

```bash
shadowlogic parse [--tool <tool_name>] --file <file_path>
```

**Parameters**:

*   `-tl, --tool <tool_name>`: Optional, the name of the scanning tool (defaults to `nmap`). Currently supported: `nmap`, `zap`.
*   `-f, --file <file_path>`: Required, the path to the output file from the scanning tool.

**Examples**:

*   Parse Nmap scan results:
    ```bash
    shadowlogic parse --tool nmap --file nmap_full_scan.xml
    ```

*   Parse OWASP ZAP scan results:
    ```bash
    shadowlogic parse --tool zap --file zap_report.json
    ```
