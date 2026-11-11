from fastapi import FastAPI
from sqlmodel import Session , select
from contextlib import asynccontextmanager
from database import create_db_and_tables, engine
from fastapi.middleware.cors import CORSMiddleware

from models import Player

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


origins = [
    "http://localhost:3000",  # React development server
    "https://example.com",    # Production frontend
    "*"
] # Define allowed origins (domains that can access your API)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # Allow these origins
    allow_credentials=True,       # Allow cookies, authentication headers
    allow_methods=["*"],          # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],          # Allow all headers
)



@app.get("/")
async def root():
    return {"message": "Welcome to Tevyat, Traveler!"}


@app.get("/player/{id}")
async def read_player(id):
    with Session(engine) as session:
        print(id,'--------------------------------------------------------------')
        player = session.get(Player, id)
        return {"message": player}
    

@app.post("/player")
async def root(player  : Player):
    with Session(engine) as session:
        session.add(player)
        session.commit()
        session.refresh(player)
        return {"message": player}
    