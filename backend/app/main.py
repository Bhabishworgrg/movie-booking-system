from fastapi import FastAPI, APIRouter 
from fastapi.responses import RedirectResponse

from app.routers import *
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

router = APIRouter(prefix=settings.API_PREFIX)
router.include_router(movie)
router.include_router(showtime)
router.include_router(booking)
router.include_router(seat)
router.include_router(auth)
router.include_router(user)

app.include_router(router)

@app.get('/', include_in_schema=False)
def root():
    return RedirectResponse('/docs')
