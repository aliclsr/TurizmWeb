from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from app import models
from app.database import engine
from app.routers import iletisim


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(iletisim.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/about", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("hakkimizda.html", {"request": request})


@app.get("/services", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("hizmetlerimiz.html", {"request": request})


@app.get("/contact", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("iletisim.html", {"request": request})
