from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def display_report(report, overall, recommendation):

    # ----------------------------
    # Score Summary Table
    # ----------------------------

    table = Table(title="📋 Interview Summary")

    table.add_column("Metric", style="cyan", justify="left")
    table.add_column("Value", style="green", justify="center")

    table.add_row(
        "Technical Score",
        f"{report['technical_score']}/10"
    )

    table.add_row(
        "Communication Score",
        f"{report['communication_score']}/10"
    )

    table.add_row(
        "Confidence Score",
        f"{report['confidence_score']}/10"
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

    # ----------------------------
    # Strengths
    # ----------------------------

    if report["strengths"]:

        console.print(
            Panel(
                "\n".join(
                    f"✔ {item}"
                    for item in report["strengths"]
                ),
                title="💪 Strengths",
                border_style="green",
            )
        )

    # ----------------------------
    # Weaknesses
    # ----------------------------

    if report["weaknesses"]:

        console.print(
            Panel(
                "\n".join(
                    f"• {item}"
                    for item in report["weaknesses"]
                ),
                title="⚠ Weaknesses",
                border_style="red",
            )
        )

    # ----------------------------
    # Missing Concepts
    # ----------------------------

    if report["missing_concepts"]:

        console.print(
            Panel(
                "\n".join(
                    f"• {item}"
                    for item in report["missing_concepts"]
                ),
                title="📚 Missing Concepts",
                border_style="yellow",
            )
        )