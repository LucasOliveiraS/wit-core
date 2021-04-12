import sys
import click

[sys.path.append(i) for i in ['.', '..']]
from wit_core.core.process import process_intent


@click.command()
def shell():
    click.echo("Type a message and press enter to process it.")
    while True:
        try:
            message = input("> ")
        except (EOFError, KeyboardInterrupt):
            click.echo("Closing command line chat...")
            break

        response = process_intent(message)
        click.echo(response)
        click.echo("Next message:")
