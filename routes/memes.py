import requests
import random

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from rich.console import Console

# --- Constants --- #

app = APIRouter(tags=["MEMES"], prefix="/memes")
templates = Jinja2Templates(directory="templates")
console = Console()

# --- Routes --- #

@app.get("/")
async def memepage(request: Request, types: str) -> dict:
    types = types.split(",")[:-1]
    meme_list = gen_list(types)

    if isinstance(meme_list, dict):
        return {"status": 404, "reason": f"Invalid meme type {meme_list['type']}"}
    
    return templates.TemplateResponse("memesredir.html", {
        "request": request,
        "meme_list": meme_list
    })


    
# --- Helpers --- #

def gen_list(types: list[str]) -> list[str]:
    # Verifying all the types
    valid_types = ["memes", "funny", "animememes", "AdviceAnimals", "MemeEconomy", "dankmemes", "MinecraftMemes", "programmingmemes", "softwaregore"]
    for type_ in types:
        if type_ not in valid_types:
            return {"type": type_}
    
    # Grabbing the meme list
    meme_list = []
    for type_ in types:
        resp = requests.get(
            f"https://www.reddit.com/r/{type_}.json",
            headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
        )
        links = resp.json()["data"]["children"]
        [meme_list.append([type_, link["data"]["title"], link["data"]["url"]]) for link in links if link["data"]["url"].endswith((".jpg", ".gif", ".png"))]
    
    random.shuffle(meme_list)
    return meme_list


# -------------- #