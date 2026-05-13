import os
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Read the environment variable, default to a local SQLite file
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "sqlite:///./local_chat_history.db" # The local fallback
)

# 2. SQLite requires a specific argument to work with FastAPI's threads
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    # This block will run in AWS when you provide the Postgres URL
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ChatHistory(Base):
    __tablename__ = "chats"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50))
    user_msg = Column(Text)
    ai_msg = Column(Text)

# 3. Create the tables (this creates the .db file locally)
Base.metadata.create_all(bind=engine)