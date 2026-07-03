import argparse
import textwrap

import rich_argparse

from task.settings import clear


def build_parser() -> None:
    parser = argparse.ArgumentParser(
        prog="task",
        description=textwrap.dedent("""
        Task Manager helps you organize your tasks directly from the terminal.

        You can create, search, list, and delete tasks with ease - all from
        your CLI. No need for web apps, mouse clicks or distractions.
        Just productivity.
        """),
        epilog=textwrap.dedent("""
        This will be shown below all arguments and can be used to add
        copyright or other complex examples.
        """),
        formatter_class=rich_argparse.RawDescriptionRichHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser(
        "create",
        aliases=["new", "add"],
        description=textwrap.dedent("""
        Use this command to create a new task quickly and efficiently.

        Provide a title, optional tags, priority, and mark it as done if needed.
        Whether you're planning your day or dumping ideas into the terminal,
        this is your entry point."""),
        epilog=textwrap.dedent("""
        Examples:

        task create -t "Buy groceries"
        task create -t "Study argparse" --tag python --tag cli --priority high
        task create -t "Walk the dog" --done

        You can also combine options freely to match your workflow.
        Tags help with filtering later. Priorities can be: low, medium, high."""),
        formatter_class=rich_argparse.RawDescriptionRichHelpFormatter,
    )

    return parser


def run() -> None:
    clear()  # limpa o terminal
    parser = build_parser()

    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    # entry point ao usar o módulo diretamente
    run()
