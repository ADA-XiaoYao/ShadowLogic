import click
from rich.console import Console
from rich.panel import Panel
from rich.markup import escape
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
from src.shadowspear.payload_generation_engine import PayloadGenerationEngine
from src.shadowspear.attack_workflow_orchestrator import AttackWorkflowOrchestrator
from src.shadowspear.target_ai_model_interface import TargetAIModelInterface
from src.shadowshield.model_analysis_engine import ModelAnalysisEngine
from src.shadowshield.vulnerability_scanner_core import VulnerabilityScannerCore
from src.shadowshield.ai_security_policy_engine import AISecurityPolicyEngine
from src.shadowshield.remediation_hardening_advisor import RemediationHardeningAdvisor

console = Console()

@click.group()
def cli():
    """ShadowLogic: An AI-powered command-line penetration testing assistant tool."""
    pass

@cli.group()
def shadowspear():
    """ShadowSpear: The Attacker's Toolkit for AI security."""
    pass

@shadowspear.group()
def payload_gen():
    """Payload generation commands."""
    pass

@payload_gen.command()
@click.option("--target-llm-context", "-t", required=True, help="Description of the target LLM's purpose, typical prompts, and known defenses.")
@click.option("--objective", "-o", required=True, help="The desired outcome of the injection (e.g., extract data, bypass safety filters, execute code).")
@click.option("--evasion-techniques", "-e", multiple=True, help="List of evasion techniques to incorporate (e.g., obfuscation, character substitution).")
def prompt_injection(target_llm_context, objective, evasion_techniques):
    """Generates a prompt injection payload for a target LLM."""
    engine = PayloadGenerationEngine()
    console.print("[bold blue]ShadowSpear is generating prompt injection payload...[/bold blue]")
    result = engine.generate_prompt_injection_payload(target_llm_context, objective, list(evasion_techniques))
    console.print(Panel(escape(result), title="[bold green]ShadowSpear Prompt Injection Payload[/bold green]"))

@payload_gen.command()
@click.option("--target-model-type", "-m", required=True, help="Type of the target ML model (e.g., 'image classifier', 'sentiment analysis').")
@click.option("--target-input-data", "-i", required=True, help="Description or example of the input data the model expects.")
@click.option("--objective", "-o", required=True, help="The desired misclassification or model behavior.")
@click.option("--constraints", "-c", help="Any constraints on the adversarial example (e.g., 'imperceptible to human eye').")
def adversarial_example(target_model_type, target_input_data, objective, constraints):
    """Generates an adversarial example for a target ML model."""
    engine = PayloadGenerationEngine()
    console.print("[bold blue]ShadowSpear is generating adversarial example...[/bold blue]")
    result = engine.generate_adversarial_example(target_model_type, target_input_data, objective, constraints)
    console.print(Panel(escape(result), title="[bold green]ShadowSpear Adversarial Example[/bold green]"))

@payload_gen.command()
@click.option("--target-model-type", "-m", required=True, help="Type of the target ML model.")
@click.option("--target-dataset-context", "-d", required=True, help="Description of the target model's training dataset.")
@click.option("--objective", "-o", required=True, help="The desired long-term impact on the model's behavior.")
@click.option("--impact-description", "-i", help="Detailed description of the intended impact.")
def data_poisoning(target_model_type, target_dataset_context, objective, impact_description):
    """Generates a data poisoning sample for a target ML model's training data."""
    engine = PayloadGenerationEngine()
    console.print("[bold blue]ShadowSpear is generating data poisoning sample...[/bold blue]")
    result = engine.generate_data_poisoning_sample(target_model_type, target_dataset_context, objective, impact_description)
    console.print(Panel(escape(result), title="[bold green]ShadowSpear Data Poisoning Sample[/bold green]"))

@shadowspear.group()
def workflow():
    """Attack workflow commands."""
    pass

@workflow.command()
@click.option("--target-llm-context", "-t", required=True, help="Description of the target LLM.")
@click.option("--objective", "-o", required=True, help="The desired outcome of the injection.")
@click.option("--initial-payload", "-i", help="An initial payload to start with.")
@click.option("--max-iterations", "-m", type=int, default=3, help="Maximum number of attempts to refine the payload.")
def prompt_injection_workflow(target_llm_context, objective, initial_payload, max_iterations):
    """Runs a multi-step prompt injection workflow, adapting based on LLM responses."""
    orchestrator = AttackWorkflowOrchestrator()
    console.print("[bold blue]ShadowSpear is running prompt injection workflow...[/bold blue]")
    result = orchestrator.run_prompt_injection_workflow(target_llm_context, objective, initial_payload, max_iterations)
    console.print(Panel(escape(result), title="[bold green]ShadowSpear Prompt Injection Workflow Result[/bold green]"))

@shadowspear.group()
def api_interact():
    """AI Model API interaction commands."""
    pass

@api_interact.command()
@click.option("--api-endpoint", "-e", required=True, help="The URL of the LLM API endpoint.")
@click.option("--prompt", "-p", required=True, help="The prompt to send to the LLM.")
@click.option("--api-key", "-k", help="API key for authentication.")
@click.option("--model-name", "-m", default="gpt-4", help="The name of the LLM model to use.")
@click.option("--temperature", "-t", type=float, default=0.7, help="Controls randomness in generation.")
def llm(api_endpoint, prompt, api_key, model_name, temperature):
    """Interacts with a generic LLM API endpoint."""
    interface = TargetAIModelInterface()
    console.print(f"[bold blue]ShadowSpear is interacting with LLM API at {api_endpoint}...[/bold blue]")
    result = interface.interact_llm_api(api_endpoint, prompt, api_key, model_name, temperature)
    console.print(Panel(str(result), title="[bold green]ShadowSpear LLM API Interaction Result[/bold green]"))

@api_interact.command()
@click.option("--api-endpoint", "-e", required=True, help="The URL of the custom API endpoint.")
@click.option("--data", "-d", required=True, help="The JSON data payload to send.")
@click.option("--headers", "-H", help="Custom headers for the request (JSON string).")
@click.option("--method", "-M", default="POST", help="HTTP method (e.g., 'POST', 'GET').")
def custom(api_endpoint, data, headers, method):
    """Interacts with a custom AI model API endpoint."""
    interface = TargetAIModelInterface()
    console.print(f"[bold blue]ShadowSpear is interacting with custom AI API at {api_endpoint}...[/bold blue]")
    try:
        data_dict = json.loads(data)
        headers_dict = json.loads(headers) if headers else None
        result = interface.interact_custom_api(api_endpoint, data_dict, headers_dict, method)
        console.print(Panel(str(result), title="[bold green]ShadowSpear Custom API Interaction Result[/bold green]"))
    except json.JSONDecodeError as e:
        console.print(Panel(f"[bold red]Error parsing JSON input: {e}[/bold red]", title="[bold red]Error[/bold red]"))

@cli.group()
def shadowshield():
    """ShadowShield: The Defender's Scanner for AI security."""
    pass

@shadowshield.group()
def model_analysis():
    """AI Model analysis commands."""
    pass

@model_analysis.command()
@click.option("--model-architecture-description", "-m", required=True, help="A high-level description of the model's architecture and purpose.")
@click.option("--graph-representation", "-g", help="A (simulated) representation of the computational graph.")
@click.option("--context", "-c", help="Additional context about the model or potential threats.")
def analyze_graph(model_architecture_description, graph_representation, context):
    """Analyzes the computational graph of an AI model to detect backdoors or unusual logic flows."""
    engine = ModelAnalysisEngine()
    console.print("[bold blue]ShadowShield is analyzing computational graph...[/bold blue]")
    result = engine.analyze_computational_graph(model_architecture_description, graph_representation, context)
    console.print(Panel(escape(result), title="[bold green]ShadowShield Computational Graph Analysis Result[/bold green]"))

@model_analysis.command()
@click.option("--dataset-description", "-d", required=True, help="A description of the training dataset.")
@click.option("--data-samples", "-s", help="Representative samples of the training data.")
@click.option("--context", "-c", help="Additional context about the data collection or labeling process.")
def audit_data(dataset_description, data_samples, context):
    """Audits the training data of an AI model to identify data poisoning or bias."""
    engine = ModelAnalysisEngine()
    console.print("[bold blue]ShadowShield is auditing training data...[/bold blue]")
    result = engine.audit_training_data(dataset_description, data_samples, context)
    console.print(Panel(escape(result), title="[bold green]ShadowShield Training Data Audit Result[/bold green]"))

@shadowshield.group()
def vulnerability_scan():
    """AI Vulnerability scanning commands."""
    pass

@vulnerability_scan.command()
@click.option("--target-llm-application-description", "-t", required=True, help="Description of the target LLM application.")
@click.option("--test-prompts", "-p", multiple=True, help="A list of specific prompts to test (JSON string).")
@click.option("--context", "-c", help="Additional context about the application or known vulnerabilities.")
def prompt_injection_scan(target_llm_application_description, test_prompts, context):
    """Scans an AI application for susceptibility to prompt injection attacks."""
    core = VulnerabilityScannerCore()
    console.print("[bold blue]ShadowShield is scanning for prompt injection vulnerabilities...[/bold blue]")
    result = core.scan_prompt_injection(target_llm_application_description, list(test_prompts) if test_prompts else None, context)
    console.print(Panel(escape(result), title="[bold green]ShadowShield Prompt Injection Scan Result[/bold green]"))

@vulnerability_scan.command()
@click.option("--target-model-description", "-m", required=True, help="Description of the target AI model.")
@click.option("--input-data-type", "-i", required=True, help="The type of input data the model processes.")
@click.option("--attack-scenarios", "-a", multiple=True, help="Specific adversarial attack scenarios to simulate (JSON string).")
@click.option("--context", "-c", help="Additional context about the model or its deployment environment.")
def adversarial_robustness(target_model_description, input_data_type, attack_scenarios, context):
    """Assesses the robustness of an AI model against adversarial examples."""
    core = VulnerabilityScannerCore()
    console.print("[bold blue]ShadowShield is assessing adversarial robustness...[/bold blue]")
    result = core.assess_adversarial_robustness(target_model_description, input_data_type, list(attack_scenarios) if attack_scenarios else None, context)
    console.print(Panel(escape(result), title="[bold green]ShadowShield Adversarial Robustness Assessment Result[/bold green]"))

@shadowshield.group()
def policy_engine():
    """AI Security Policy Engine commands."""
    pass

@policy_engine.command()
@click.option("--model-description", "-m", required=True, help="Description of the AI model.")
@click.option("--deployment-environment-description", "-d", required=True, help="Description of the deployment environment.")
@click.option("--policy-standards", "-p", multiple=True, help="List of specific policy standards or best practices to check against (JSON string).")
@click.option("--context", "-c", help="Additional context about the organization's security posture or specific concerns.")
def evaluate_compliance(model_description, deployment_environment_description, policy_standards, context):
    """Evaluates AI models and deployments against established security policies and best practices."""
    engine = AISecurityPolicyEngine()
    console.print("[bold blue]ShadowShield is evaluating policy compliance...[/bold blue]")
    result = engine.evaluate_policy_compliance(model_description, deployment_environment_description, list(policy_standards) if policy_standards else None, context)
    console.print(Panel(escape(result), title="[bold green]ShadowShield Policy Compliance Report[/bold green]"))

@shadowshield.group()
def advisor():
    """Remediation and Hardening Advisor commands."""
    pass

@advisor.command()
@click.option("--vulnerability-details", "-v", required=True, help="Detailed description of the identified vulnerability.")
@click.option("--model-type", "-m", required=True, help="Type of the AI model.")
@click.option("--deployment-context", "-d", required=True, help="Description of the deployment environment.")
@click.option("--context", "-c", help="Additional context about the system or existing security controls.")
def remediation_advice(vulnerability_details, model_type, deployment_context, context):
    """Provides actionable advice for mitigating identified vulnerabilities."""
    advisor = RemediationHardeningAdvisor()
    console.print("[bold blue]ShadowShield is generating remediation advice...[/bold blue]")
    result = advisor.get_remediation_advice(vulnerability_details, model_type, deployment_context, context)
    console.print(Panel(escape(result), title="[bold green]ShadowShield Remediation Advice[/bold green]"))

@advisor.command()
@click.option("--model-type", "-m", required=True, help="Type of the AI model.")
@click.option("--deployment-context", "-d", required=True, help="Description of the deployment environment.")
@click.option("--security-goals", "-s", multiple=True, help="Specific security goals (JSON string).")
@click.option("--context", "-c", help="Additional context about the system.")
def hardening_guidelines(model_type, deployment_context, security_goals, context):
    """Provides general hardening guidelines for AI systems."""
    advisor = RemediationHardeningAdvisor()
    console.print("[bold blue]ShadowShield is generating hardening guidelines...[/bold blue]")
    result = advisor.get_hardening_guidelines(model_type, deployment_context, list(security_goals) if security_goals else None, context)
    console.print(Panel(escape(result), title="[bold green]ShadowShield Hardening Guidelines[/bold green]"))

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
