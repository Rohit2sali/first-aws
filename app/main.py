from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import SessionLocal, ChatHistory
# 1. IMPORT THE LLM HERE:
from app.model_loader import llm 

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class ChatRequest(BaseModel):
    user_id: str
    message: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def get_frontend(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/chat")
async def chat(chat_req: ChatRequest, db: Session = Depends(get_db)):
    
    # 2. USE THE ACTUAL MODEL HERE:
    print("🧠 Thinking...")
    response_text = llm.generate_response(chat_req.message)
    print("✅ Done!")
    
    # Store in Database
    new_chat = ChatHistory(
        user_id=chat_req.user_id, 
        user_msg=chat_req.message, 
        ai_msg=response_text
    )
    db.add(new_chat)
    db.commit()
    
    return {"response": response_text}