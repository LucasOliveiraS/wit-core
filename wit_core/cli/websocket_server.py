import click
import uvicorn


@click.command()
@click.option('--port', default=8000, help='Websocket server port')
def websocket_server(port):
    uvicorn.run(
        "wit_core.api.websocket_server:app",
        host="0.0.0.0", port=port,
        reload=True
    )
