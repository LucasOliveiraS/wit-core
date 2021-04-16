#!/usr/bin/env python
import sys
import click

[sys.path.append(i) for i in ['.', '..']]
from wit_core.cli.scafolld import init
from wit_core.cli.shell import shell
from wit_core.cli.http_server import http_server
from wit_core.cli.websocket_server import websocket_server


@click.group()
def cli():
    pass


cli.add_command(init)
cli.add_command(shell)
cli.add_command(http_server)
cli.add_command(websocket_server)


def main():
    cli()


if __name__ == '__main__':
    main()
