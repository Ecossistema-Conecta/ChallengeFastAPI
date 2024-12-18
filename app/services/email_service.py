import logging
import os

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from fastapi import HTTPException
from jinja2 import Environment, FileSystemLoader, select_autoescape

from app.utils.constants import SENDGRID_API_KEY

env = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), "..", "templates")),
    autoescape=select_autoescape(['html'])
)


def render_email_template(template_name: str, context: dict) -> str:
    template = env.get_template(template_name)
    return template.render(**context)


def send_email(to: list, subject: str, body: str):
    message = Mail(
        from_email="limapguilherme@hotmail.com",
        to_emails=to,
        subject=subject,
        html_content=body
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
    except Exception as e:
        logging.exception("Erro ao enviar email:", e)
        raise HTTPException(status_code=500, detail="Falha ao enviar email.")

