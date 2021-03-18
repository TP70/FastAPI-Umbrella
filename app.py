import fastapi
import uvicorn

from api import whether_api
from views import home

api = fastapi.FastAPI()


def configure():
    api.include_router(home.router)
    api.include_router(whether_api.router)


configure()
if __name__ == '__main__':
    uvicorn.run(api, debug=True)

