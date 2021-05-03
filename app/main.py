import pathlib

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/countup", response_class=HTMLResponse)
async def render_countup(
    request: Request, _round: int = Form(...), total_score: int = Form(0), score: int = Form(0)
):
    _round += 1
    total_score += score
    if _round <= 8:
        return templates.TemplateResponse(
            "countup.html", {"request": request, "_round": _round, "total_score": total_score}
        )
    else:
        avg = round(total_score / 8)
        return templates.TemplateResponse(
            "result.html", {"request": request, "total_score": total_score, "avg": avg}
        )
