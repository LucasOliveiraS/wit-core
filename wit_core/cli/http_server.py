import click
import uvicorn


@click.command()
@click.option('--port', default=8000, help='HTTP server port')
def http_server(port):
    uvicorn.run(
        "wit_core.api.http_server:app",
        host="0.0.0.0", port=port,
        reload=True
    )
