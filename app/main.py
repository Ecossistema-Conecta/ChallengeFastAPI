from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()


templates = Jinja2Templates(directory="app/templates")

app.mount("/static", StaticFiles(directory="app/static", html=True), name="static")

@app.get("/challenge", response_class=HTMLResponse)
async def challenge(request: Request, step: int | None = None):
    if not step or step != 1:
        return templates.TemplateResponse("challenge_overview.html", {"request": request, "step": None, "next_step": 1})

    return templates.TemplateResponse(f"challenge_step{step}.html",
                                      {"request": request, "step": step, "next_step": step + 1})
