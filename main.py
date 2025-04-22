from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
from chatbot import generate_response
from database import init_db, save_log

app = FastAPI()
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
static_path = os.path.join(current_dir)
templates_path = os.path.join(current_dir)
print(f"Static files path: {static_path}")
print(f"Templates path: {templates_path}")
print(f"Directory exists (static): {os.path.exists(static_path)}")
print(f"Directory exists (templates): {os.path.exists(templates_path)}")
app.mount("/static", StaticFiles(directory=static_path), name="static")
templates = Jinja2Templates(directory=templates_path)

init_db()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

from fastapi import Body

@app.post("/chat")
async def chat(user_input: str = Body(..., embed=True)):
    bot_response = generate_response(user_input)
    save_log(user_input, bot_response, datetime.now().isoformat())
    return {"response": bot_response}
