import pkg_resources
from pathlib import Path
from distutils.dir_util import copy_tree
import click


def scaffold_path() -> str:
    return pkg_resources.resource_filename(__name__, "initial_project")


@click.command()
def init(path: str = str(Path.cwd())) -> None:
    copy_tree(scaffold_path(), path)
