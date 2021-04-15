import click
import uvicorn


@click.command()
def http_server():
    uvicorn.run(
        "wit_core.api.http_server:app",
        host="0.0.0.0", port=8000,
        reload=True
    )
