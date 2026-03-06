from fastapi import APIRouter

from src.api.routs.deployments.deploymentsFunctions import IsNameOk, add_new_row_to_deployment, \
    create_new_deployment_mongo, deployments_parts, change_status

deployments_router = APIRouter(prefix="/deployments_router")


@deployments_router.post("/")
def create_deployment(db_name:str, user_name:str):
    if IsNameOk(db_name, user_name):
        create_new_deployment_mongo(db_name)
        return add_new_row_to_deployment(db_name, user_name)
    else:
        return deployments_router.responses(status_code=422)



@deployments_router.get("/")
def get_deployments(id: str):
    return deployments_parts(id)

@deployments_router.delete("/")
def delete_deployment(id: str):
    part:dict = deployments_parts(id)
    print(part)
    db_name:str = part["db_name"]
    delete_deployment(db_name)
    change_status(id)
    return deployments_router.responses(status_code=204)


