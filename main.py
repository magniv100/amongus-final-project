import uvicorn
from fastapi import FastAPI

from src.api.routs.deployments.DeploymentsRout import deployments_router

app = FastAPI()
app.include_router(deployments_router)


if __name__ == '__main__':
    config = uvicorn.Config(app, port=8080)
    server = uvicorn.Server(config)
    server.run()

