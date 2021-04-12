#!/usr/bin/env python
import sys
import click

[sys.path.append(i) for i in ['.', '..']]
from wit_core.cli.scafolld import init
from wit_core.cli.shell import shell


@click.group()
def cli():
    pass


cli.add_command(shell)
cli.add_command(init)

if __name__ == '__main__':
    cli()
