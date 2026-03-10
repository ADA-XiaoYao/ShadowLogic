import click
from rich.console import Console
from rich.panel import Panel
from src.llm_agent import LLMAgent
from src.modules.vulnerability_analyzer import VulnerabilityAnalyzer
from src.modules.payload_generator import PayloadGenerator
from src.modules.scanner_integrator import ScannerIntegrator
from src.modules.report_generator import ReportGenerator

console = Console()

@click.group()
def cli():
    """ShadowLogic: 一个基于 AI 的命令行渗透测试辅助工具。"""
    pass

@cli.command()
@click.option('--target', '-t', help='扫描的目标 (如 IP, 域名)')
@click.option('--input-file', '-f', help='包含扫描结果的文件 (如 Nmap 输出)')
def analyze(target, input_file):
    """分析目标或扫描结果中的潜在漏洞。"""
    analyzer = VulnerabilityAnalyzer()
    if input_file:
        try:
            with open(input_file, 'r') as f:
                data = f.read()
            console.print(f"[bold blue]ShadowLogic 正在分析文件: {input_file}...[/bold blue]")
            result = analyzer.analyze_scan_data(data)
        except Exception as e:
            console.print(f"[red]读取文件失败: {str(e)}[/red]")
            return
    elif target:
        console.print(f"[bold blue]ShadowLogic 正在分析目标: {target}...[/bold blue]")
        result = analyzer.analyze_target(target)
    else:
        console.print("[red]错误: 请提供目标 (--target) 或输入文件 (--input-file)。[/red]")
        return
    
    console.print(Panel(result, title="[bold green]ShadowLogic AI 分析结果[/bold green]"))

@cli.command()
@click.argument('vulnerability_type')
@click.option('--context', '-c', help='漏洞的上下文信息 (如 参数名, 注入点)')
def payload(vulnerability_type, context):
    """根据漏洞类型和上下文生成 Payload。"""
    generator = PayloadGenerator()
    console.print(f"[bold blue]ShadowLogic 正在为 {vulnerability_type} 生成 Payload...[/bold blue]")
    result = generator.generate(vulnerability_type, context)
    console.print(Panel(result, title="[bold green]ShadowLogic 生成的 Payload[/bold green]"))

@cli.command()
@click.argument('prompt')
def ask(prompt):
    """直接向 ShadowLogic AI 提问渗透测试相关问题。"""
    agent = LLMAgent()
    console.print(f"[bold blue]正在咨询 ShadowLogic AI: {prompt}...[/bold blue]")
    result = agent.ask(prompt)
    console.print(Panel(result, title="[bold green]ShadowLogic AI 回答[/bold green]"))

@cli.command()
@click.option('--target', '-t', required=True, help='渗透测试目标')
@click.option('--vulnerabilities', '-v', required=True, help='发现的漏洞列表')
@click.option('--summary', '-s', required=True, help='测试总结')
def report(target, vulnerabilities, summary):
    """根据发现的漏洞生成渗透测试报告。"""
    generator = ReportGenerator()
    console.print(f"[bold blue]正在为 {target} 生成报告...[/bold blue]")
    result = generator.generate_markdown_report(target, vulnerabilities, summary)
    console.print(f"[bold green]{result}[/bold green]")

@cli.command()
@click.option('--tool', '-tl', default='nmap', help='扫描工具名称 (默认为 nmap)')
@click.option('--file', '-f', required=True, help='扫描输出文件路径')
def parse(tool, file):
    """解析扫描工具的输出并提供分析建议。"""
    integrator = ScannerIntegrator()
    try:
        with open(file, 'r') as f:
            data = f.read()
        console.print(f"[bold blue]正在解析 {tool} 输出: {file}...[/bold blue]")
        if tool.lower() == 'nmap':
            result = integrator.parse_nmap(data)
        elif tool.lower() == 'zap':
            result = integrator.parse_zap(data)
        else:
            result = integrator.parse_generic(tool, data)
        console.print(Panel(result, title=f"[bold green]ShadowLogic {tool} 解析结果[/bold green]"))
    except Exception as e:
        console.print(f"[red]解析失败: {str(e)}[/red]")

if __name__ == '__main__':
    cli()
