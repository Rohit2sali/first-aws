from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from app.db.database import engine
from app.db.models import Base

from app.auth.routes import router as auth_router
from app.chat.routes import router as chat_router
from app.uploads.routes import router as upload_router



app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
def startup_event():

    Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(chat_router)
app.include_router(upload_router)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request,
        "index.html"
    )
# from fastapi import FastAPI

# from app.db.database import engine
# from app.db.models import Base

# from app.auth.routes import router as auth_router
# from app.chat.routes import router as chat_router
# from app.uploads.routes import router as upload_router

# from app.aws.s3_utils import download_model


# app = FastAPI()


# @app.on_event("startup")
# def startup_event():

#     Base.metadata.create_all(bind=engine)

#     download_model()

# app.include_router(auth_router)
# app.include_router(chat_router)
# app.include_router(upload_router)


# @app.get("/")
# def root():
#     return {"message": "AI Backend Running"}
