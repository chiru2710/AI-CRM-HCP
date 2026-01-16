from fastapi import APIRouter
from schemas import InteractionCreate
from database import SessionLocal
from models import Interaction
from langgraph_agent import process_chat_interaction

router = APIRouter()

@router.post("/log-interaction/")
def log_interaction(data: InteractionCreate):
    db = SessionLocal()

    interaction = Interaction(
        hcp_name=data.hcp_name,
        interaction_type=data.interaction_type,
        purpose=data.purpose,
        samples_given=data.samples_given,
        follow_up_date=data.follow_up_date,
        summary="Logged via Form",
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return {"message": "Logged via form", "id": str(interaction.id)}

@router.post("/chat-log/")
def chat_log(text: str):
    return process_chat_interaction(text)

@router.get("/history/{hcp_name}")
def get_history(hcp_name: str):
    db = SessionLocal()
    interactions = db.query(Interaction).filter(Interaction.hcp_name == hcp_name).all()

    results = []
    for i in interactions:
        results.append({
            "id": str(i.id),
            "hcp_name": i.hcp_name,
            "interaction_type": i.interaction_type,
            "purpose": i.purpose,
            "samples_given": i.samples_given,
            "follow_up_date": i.follow_up_date,
            "summary": i.summary,
            "created_at": str(i.created_at),
        })

    return results
