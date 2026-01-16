from pydantic import BaseModel

class InteractionCreate(BaseModel):
    hcp_name: str
    interaction_type: str
    purpose: str
    samples_given: bool
    follow_up_date: str
