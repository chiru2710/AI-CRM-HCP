from database import SessionLocal
from models import Interaction

# ---------- TOOL 1: LOG INTERACTION (MANDATORY) ----------
def log_interaction_tool(data: dict):
    db = SessionLocal()

    interaction = Interaction(
        hcp_name=data.get("hcp_name"),
        interaction_type=data.get("interaction_type"),
        purpose=data.get("purpose"),
        samples_given=data.get("samples_given"),
        follow_up_date=data.get("follow_up_date"),
        summary=data.get("summary", "Logged via AI"),
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return {"message": "Interaction logged successfully", "id": str(interaction.id)}

# ---------- TOOL 2: EDIT INTERACTION (MANDATORY) ----------
def edit_interaction_tool(interaction_id: str, updates: dict):
    db = SessionLocal()

    interaction = db.query(Interaction).filter(Interaction.id == interaction_id).first()

    if not interaction:
        return {"error": "Interaction not found"}

    for key, value in updates.items():
        setattr(interaction, key, value)

    db.commit()
    return {"message": "Interaction updated successfully"}

# ---------- TOOL 3: FETCH HISTORY ----------
def fetch_history_tool(hcp_name: str):
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
