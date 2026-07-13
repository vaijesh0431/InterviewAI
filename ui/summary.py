from rich.console import Console
from rich.table import Table

console = Console()


def show_summary(
    duration,
    questions,
    followups,
    overall,
    recommendation,
):

    table = Table(
        title="🎯 Interview Completed",
        show_header=False
    )

    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row(
        "Duration",
        f"{duration:.2f} minutes"
    )

    table.add_row(
        "Questions",
        str(questions)
    )

    table.add_row(
        "Follow-ups",
        str(followups)
    )

    table.add_row(
        "Overall Score",
        f"{overall}/10"
    )

    table.add_row(
        "Recommendation",
        recommendation
    )

    console.print(table)