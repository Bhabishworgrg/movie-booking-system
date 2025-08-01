from fastapi import FastAPI, APIRouter 
from fastapi.responses import RedirectResponse

from app.routers import *

app = FastAPI()

router = APIRouter()
router.include_router(movie)
router.include_router(showtime)
router.include_router(booking)
router.include_router(seat)

app.include_router(router)

@app.get('/', include_in_schema=False)
def root():
    return RedirectResponse('/docs')
