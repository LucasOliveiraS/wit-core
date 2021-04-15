import click
import uvicorn


@click.command()
def websocket_server():
    uvicorn.run(
        "wit_core.api.websocket_server:app",
        host="0.0.0.0", port=8080,
        reload=True
    )
