from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import without dots (absolute imports)
from database import Base, engine
from routes import router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow React frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
