from gc import collect
import random

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
#python -m uvicorn main:app --reload

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "91215 servers"}
    )

@app.get("/gambling")
def gambling_page(request: Request, bet: int, balance: int):
    correct = random.randint(1, 30)
    if bet==0:
        correct=0
    if bet!=correct and bet!=0:
        balance -= 1
    if bet==correct and bet!=0:
        balance += 20
    return templates.TemplateResponse("gambling.html", {
        "request": request,
        "bet": bet,
        "correct": correct,
        "balance": balance
    })