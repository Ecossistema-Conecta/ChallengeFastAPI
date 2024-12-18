from fastapi import APIRouter, FastAPI, Form, HTTPException

from app.services.email_service import send_email, render_email_template
from app.utils.constants import Routes, STEP_MENTOR_EMAILS

router = APIRouter()

@router.post(Routes.FEEDBACK)
async def feedback(step: int = Form(...), comment: str = Form(...)):
    emails = STEP_MENTOR_EMAILS.get(step)

    if not emails:
        raise HTTPException(status_code=400, detail="O monitor dessa etapa ainda não cadastrou email para receber dados.")

    body_html = render_email_template("feedback_email.html", {"step": step, "comment": comment})

    send_email(to=emails, subject=f"Feedback da Etapa {step}", body=body_html)

    return {"message": "Feedback enviado com sucesso!"}
