from rich.console import Console

console = Console()


def print_header():
    console.rule("[bold cyan]InterviewAI[/bold cyan]")


def success(message):
    console.print(f"[green]✔ {message}[/green]")


def error(message):
    console.print(f"[red]✘ {message}[/red]")


def info(message):
    console.print(f"[cyan]{message}[/cyan]")