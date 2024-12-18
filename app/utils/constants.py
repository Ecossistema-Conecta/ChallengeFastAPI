class Routes:
    CHALLENGE = "/challenge"
    CHALLENGE_STEP = "/challenge?step={step}"
    FEEDBACK = "/feedback"


class Templates:
    TEMPLATES_DIR = "app/templates/"

    CHALLENGE_OVERVIEW = "challenge_overview.html"
    CHALLENGE_STEP = "challenge_step{step}.html"


STEP_MENTOR_EMAILS = {
    1: ["diogo.nascimento@delinea.com.br"],
}

GITHUB_LINKS = {
    1: "https://github.com/Ecossistema-Conecta/WorkshopFastAPI"
}


SENDGRID_API_KEY = ""
