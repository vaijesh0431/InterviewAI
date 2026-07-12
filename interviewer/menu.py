from rich.console import Console
from rich.table import Table

console = Console()


def select_topic():

    table = Table(title="Interview Domains")

    table.add_column("Option")

    table.add_column("Topic")

    table.add_row("1", "Python")

    table.add_row("2", "Machine Learning")

    table.add_row("3", "DBMS")

    table.add_row("4", "OOP")

    table.add_row("5", "HR")

    console.print(table)

    choice = input("Choose Interview Domain: ")

    mapping = {
        "1": "python",
        "2": "ml",
        "3": "dbms",
        "4": "oop",
        "5": "hr"
    }

    return mapping.get(choice)