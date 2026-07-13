from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def show_dashboard(stats):
    """
    Display interview analytics dashboard.
    """

    table = Table(
        title="📊 Interview Analytics Dashboard",
        show_header=True,
        header_style="bold cyan"
    )

    table.add_column("Metric", style="yellow")
    table.add_column("Value", justify="center", style="green")

    table.add_row(
        "🏆 Best Score",
        f"{stats.best_score()}/10"
    )

    table.add_row(
        "📈 Average Score",
        f"{stats.average_score()}/10"
    )

    table.add_row(
        "📝 Total Interviews",
        str(stats.total_interviews())
    )

    console.print(table)

    console.print()

    console.print(
        Panel.fit(
            "✅ Analytics loaded successfully.",
            title="InterviewAI",
            border_style="green",
        )
    )