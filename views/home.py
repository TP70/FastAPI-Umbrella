import fastapi
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from models.location import Location

templates = Jinja2Templates('templates')

router = fastapi.APIRouter()


@router.get('/', response_model=Location)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
