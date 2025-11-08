from pydantic import BaseModel,Field

class CandidateScore(BaseModel):
    id : int= Field("ID of the candidate")
    score : int = Field("Score of the candidate")
    reason : str = Field("Reason for the score you assigned")