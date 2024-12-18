from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Optional

from app import templates
from app.services import challenge_service
from app.utils.constants import Routes, STEP_MENTOR_EMAILS, GITHUB_LINKS

router = APIRouter()


@router.get(Routes.CHALLENGE, response_class=HTMLResponse)
async def challenge(request: Request, step: Optional[int] = None):
    if not challenge_service.step_exists(step):
        return RedirectResponse(url=Routes.CHALLENGE, status_code=302)

    template_name = challenge_service.get_template_name(step)

    next_step = challenge_service.calculate_next_step(step)
    previous_step = challenge_service.calculate_previous_step(step)

    next_step_url = Routes.CHALLENGE_STEP.format(step=next_step) if next_step else None
    if previous_step is None and step is not None:
        previous_step_url = Routes.CHALLENGE
    elif previous_step is not None:
        previous_step_url = Routes.CHALLENGE_STEP.format(step=previous_step)
    else:
        previous_step_url = None

    emails = STEP_MENTOR_EMAILS.get(step) if step in STEP_MENTOR_EMAILS else None
    github_link = GITHUB_LINKS.get(step) if step in GITHUB_LINKS else None

    context = {
        "request": request,
        "step": step,
        "next_step": next_step,
        "previous_step": previous_step,
        "next_step_url": next_step_url,
        "previous_step_url": previous_step_url,
        "step_mentor_emails": emails,
        "github_link": github_link
    }

    return templates.TemplateResponse(template_name, context)
