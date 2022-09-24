from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from rich.console import Console

# --- Constants --- #

app = APIRouter(tags=["API"], prefix="/test")
console = Console()

# --- Routes --- #

@app.get("/")
async def ping() -> dict:
    return {"status":True}

# -------------- #