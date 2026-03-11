import click
from rich.console import Console
from rich.panel import Panel
from src.llm_agent import LLMAgent
from src.modules.vulnerability_analyzer import VulnerabilityAnalyzer
from src.modules.payload_generator import PayloadGenerator
from src.modules.scanner_integrator import ScannerIntegrator
from src.modules.report_generator import ReportGenerator
from src.modules.reconnaissance import ReconnaissanceModule
from src.modules.exploitation import ExploitationModule
from src.modules.post_exploitation import PostExploitationModule
from src.modules.attack_graph_analyzer import AttackGraphAnalyzer
from src.modules.risk_assessment_engine import RiskAssessmentEngine
from src.modules.adaptive_planner import AdaptivePlanner

console = Console()

@click.group()
def cli():
    """ShadowLogic: An AI-powered command-line penetration testing assistant tool."""
    pass

@cli.group()
def decision():
    """Intelligent decision-making and adaptive strategy commands."""
    pass

@decision.command()
@click.option("--vulnerabilities", "-v", required=True, help="Description of discovered vulnerabilities")
@click.option("--assets", "-a", required=True, help="Description of target assets")
@click.option("--network-topology", "-n", required=True, help="Description of the network topology")
@click.option("--context", "-c", help="Additional context for attack graph analysis")
def analyze_graph(vulnerabilities, assets, network_topology, context):
    """Analyzes potential attack paths based on vulnerabilities, assets, and network topology."""
    analyzer = AttackGraphAnalyzer()
    console.print("[bold blue]ShadowLogic is analyzing attack graph...[/bold blue]")
    result = analyzer.analyze_graph(vulnerabilities, assets, network_topology, context)
    console.print(Panel(result, title="[bold green]ShadowLogic Attack Graph Analysis Result[/bold green]"))

@decision.command()
@click.option("--vulnerability-details", "-v", required=True, help="Description of discovered vulnerabilities")
@click.option("--attack-path-info", "-a", required=True, help="Information about the identified attack paths")
@click.option("--context", "-c", help="Additional context for risk assessment")
def assess_risk(vulnerability_details, attack_path_info, context):
    """Dynamically assesses the risk of identified vulnerabilities and potential attack paths."""
    engine = RiskAssessmentEngine()
    console.print("[bold blue]ShadowLogic is assessing risk...[/bold blue]")
    result = engine.assess_risk(vulnerability_details, attack_path_info, context)
    console.print(Panel(result, title="[bold green]ShadowLogic Risk Assessment Result[/bold green]"))

@decision.command()
@click.option("--current-situation", "-s", required=True, help="Description of the current state of the penetration test")
@click.option("--previous-actions", "-p", required=True, help="Summary of actions taken so far")
@click.option("--feedback", "-f", required=True, help="Feedback received from the target system or tools")
@click.option("--context", "-c", help="Additional context for adaptive planning")
def adapt_plan(current_situation, previous_actions, feedback, context):
    """Adapts the attack strategy based on real-time feedback and environmental changes."""
    planner = AdaptivePlanner()
    console.print("[bold blue]ShadowLogic is adapting attack plan...[/bold blue]")
    result = planner.adapt_strategy(current_situation, previous_actions, feedback, context)
    console.print(Panel(result, title="[bold green]ShadowLogic Adaptive Plan Result[/bold green]"))

@cli.group()
def recon():
    """Reconnaissance commands."""
    pass

@recon.command()
@click.option("--target", "-t", required=True, help="Target for passive reconnaissance (e.g., domain)")
def passive(target):
    """Performs passive reconnaissance on a given target using OSINT techniques."""
    recon_module = ReconnaissanceModule()
    console.print(f"[bold blue]ShadowLogic is performing passive reconnaissance on {target}...[/bold blue]")
    result = recon_module.passive_recon(target)
    console.print(Panel(result, title="[bold green]ShadowLogic Passive Reconnaissance Result[/bold green]"))

@recon.command()
@click.option("--target", "-t", required=True, help="Target for active reconnaissance (e.g., IP, domain)")
def active(target):
    """Performs active reconnaissance on a given target (simulated Nmap)."""
    recon_module = ReconnaissanceModule()
    console.print(f"[bold blue]ShadowLogic is performing active reconnaissance on {target}...[/bold blue]")
    result = recon_module.active_recon(target)
    console.print(Panel(result, title="[bold green]ShadowLogic Active Reconnaissance Result[/bold green]"))

@recon.command()
@click.option("--domain", "-d", required=True, help="Domain for subdomain enumeration")
def subdomains(domain):
    """Enumerates subdomains for a given domain (simulated)."""
    recon_module = ReconnaissanceModule()
    console.print(f"[bold blue]ShadowLogic is enumerating subdomains for {domain}...[/bold blue]")
    result = recon_module.enumerate_subdomains(domain)
    console.print(Panel(result, title="[bold green]ShadowLogic Subdomain Enumeration Result[/bold green]"))

@cli.group()
def exploit():
    """Exploitation commands."""
    pass

@exploit.command()
@click.option("--vulnerability", "-v", required=True, help="Details of the vulnerability (e.g., CVE ID, description)")
@click.option("--target-info", "-t", help="Information about the target (e.g., OS, services)")
def identify(vulnerability, target_info):
    """Identifies potential exploits for given vulnerability details and target information."""
    exploit_module = ExploitationModule()
    console.print(f"[bold blue]ShadowLogic is identifying exploits for: {vulnerability}...[/bold blue]")
    result = exploit_module.identify_exploits(vulnerability, target_info)
    console.print(Panel(result, title="[bold green]ShadowLogic Exploit Identification Result[/bold green]"))

@exploit.command()
@click.option("--exploit-name", "-e", required=True, help="Name of the exploit to simulate")
@click.option("--target", "-t", required=True, help="Target for exploit simulation")
@click.option("--payload", "-p", help="Payload to use with the exploit")
def simulate(exploit_name, target, payload):
    """Simulates the execution of an exploit against a target."""
    exploit_module = ExploitationModule()
    console.print(f"[bold blue]ShadowLogic is simulating exploit \'{exploit_name}\' on {target}...[/bold blue]")
    result = exploit_module.simulate_exploit(exploit_name, target, payload)
    console.print(Panel(result, title="[bold green]ShadowLogic Exploit Simulation Result[/bold green]"))

@cli.group()
def post_exploit():
    """Post-exploitation commands."""
    pass

@post_exploit.command()
@click.option("--current-privileges", "-p", required=True, help="Current privileges on the compromised system")
@click.option("--target-os", "-o", required=True, help="Operating system of the target")
@click.option("--context", "-c", help="Additional context for privilege escalation")
def privesc(current_privileges, target_os, context):
    """Provides strategies for privilege escalation on a compromised system."""
    post_exploit_module = PostExploitationModule()
    console.print(f"[bold blue]ShadowLogic is generating privilege escalation strategies for {target_os}...[/bold blue]")
    result = post_exploit_module.privilege_escalation(current_privileges, target_os, context)
    console.print(Panel(result, title="[bold green]ShadowLogic Privilege Escalation Strategies[/bold green]"))

@post_exploit.command()
@click.option("--compromised-host-info", "-h", required=True, help="Information about the compromised host")
@click.option("--network-segment-info", "-n", required=True, help="Information about the network segment")
@click.option("--context", "-c", help="Additional context for lateral movement")
def lateral(compromised_host_info, network_segment_info, context):
    """Provides strategies for lateral movement within a compromised network."""
    post_exploit_module = PostExploitationModule()
    console.print(f"[bold blue]ShadowLogic is generating lateral movement strategies...[/bold blue]")
    result = post_exploit_module.lateral_movement(compromised_host_info, network_segment_info, context)
    console.print(Panel(result, title="[bold green]ShadowLogic Lateral Movement Strategies[/bold green]"))

@post_exploit.command()
@click.option("--target-data-type", "-d", required=True, help="Type of data to exfiltrate")
@click.option("--compromised-host-info", "-h", required=True, help="Information about the compromised host")
@click.option("--context", "-c", help="Additional context for data exfiltration")
def exfil(target_data_type, compromised_host_info, context):
    """Provides strategies for data exfiltration from a compromised system."""
    post_exploit_module = PostExploitationModule()
    console.print(f"[bold blue]ShadowLogic is generating data exfiltration strategies...[/bold blue]")
    result = post_exploit_module.data_exfiltration(target_data_type, compromised_host_info, context)
    console.print(Panel(result, title="[bold green]ShadowLogic Data Exfiltration Strategies[/bold green]"))

@cli.command()
@click.option("--target", "-t", help="Target for scanning (e.g., IP, domain)")
@click.option("--input-file", "-f", help="File containing scan results (e.g., Nmap output)")
def analyze(target, input_file):
    """Analyzes potential vulnerabilities in a target or scan results."""
    analyzer = VulnerabilityAnalyzer()
    if input_file:
        try:
            with open(input_file, "r") as f:
                data = f.read()
            console.print(f"[bold blue]ShadowLogic is analyzing file: {input_file}...[/bold blue]")
            result = analyzer.analyze_scan_data(data)
        except Exception as e:
            console.print(f"[red]Failed to read file: {str(e)}[/red]")
            return
    elif target:
        console.print(f"[bold blue]ShadowLogic is analyzing target: {target}...[/bold blue]")
        result = analyzer.analyze_target(target)
    else:
        console.print("[red]Error: Please provide a target (--target) or an input file (--input-file).[/red]")
        return
    
    console.print(Panel(result, title="[bold green]ShadowLogic AI Analysis Result[/bold green]"))

@cli.command()
@click.argument("vulnerability_type")
@click.option("--context", "-c", help="Context information for the vulnerability (e.g., parameter name, injection point)")
def payload(vulnerability_type, context):
    """Generates payloads based on vulnerability type and context."""
    generator = PayloadGenerator()
    console.print(f"[bold blue]ShadowLogic is generating payload for {vulnerability_type}...[/bold blue]")
    result = generator.generate(vulnerability_type, context)
    console.print(Panel(result, title="[bold green]ShadowLogic Generated Payload[/bold green]"))

@cli.command()
@click.argument("prompt")
def ask(prompt):
    """Directly asks the AI penetration testing related questions."""
    agent = LLMAgent()
    console.print(f"[bold blue]Consulting ShadowLogic AI: {prompt}...[/bold blue]")
    result = agent.ask(prompt)
    console.print(Panel(result, title="[bold green]ShadowLogic AI Response[/bold green]"))

@cli.command()
@click.option("--target", "-t", required=True, help="Penetration test target")
@click.option("--vulnerabilities", "-v", required=True, help="List of discovered vulnerabilities")
@click.option("--summary", "-s", required=True, help="Test summary")
def report(target, vulnerabilities, summary):
    """Generates a penetration test report based on discovered vulnerabilities."""
    generator = ReportGenerator()
    console.print(f"[bold blue]ShadowLogic is generating report for {target}...[/bold blue]")
    result = generator.generate_markdown_report(target, vulnerabilities, summary)
    console.print(f"[bold green]{result}[/bold green]")

@cli.command()
@click.option("--tool", "-tl", default="nmap", help="Scanner tool name (defaults to nmap)")
@click.option("--file", "-f", required=True, help="Path to the scanner output file")
def parse(tool, file):
    """Parses scanner tool output and provides analysis recommendations."""
    integrator = ScannerIntegrator()
    try:
        with open(file, "r") as f:
            data = f.read()
        console.print(f"[bold blue]ShadowLogic is parsing {tool} output: {file}...[/bold blue]")
        if tool.lower() == "nmap":
            result = integrator.parse_nmap(data)
        elif tool.lower() == "zap":
            result = integrator.parse_zap(data)
        else:
            result = integrator.parse_generic(tool, data)
        console.print(Panel(result, title=f"[bold green]ShadowLogic {tool} Analysis Result[/bold green]"))
    except Exception as e:
        console.print(f"[red]Parsing failed: {str(e)}[/red]")

if __name__ == "__main__":
    cli()
