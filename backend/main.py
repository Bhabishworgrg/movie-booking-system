from fastapi import FastAPI, APIRouter 
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get('/', include_in_schema=False)
def root():
    return RedirectResponse('/docs')
