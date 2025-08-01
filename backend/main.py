from fastapi import FastAPI, APIRouter 
from fastapi.responses import RedirectResponse

from backend.routers import movie

app = FastAPI()

router = APIRouter()
router.include_router(movie.router)

@app.get('/', include_in_schema=False)
def root():
    return RedirectResponse('/docs')
