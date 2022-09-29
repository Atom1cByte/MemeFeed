from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from rich.console import Console

# --- Constants --- #

app = APIRouter(tags=["MEME"], prefix="/meme")
templates = Jinja2Templates(directory="templates")
console = Console()

# --- Routes --- #

@app.get("/{meme_id}")
async def meme(request: Request, meme_id: int):
    return templates.TemplateResponse("memepage.html", {
        "request": request,
        "meme_id": meme_id
    })


# --- Helpers --- #



# -------------- #