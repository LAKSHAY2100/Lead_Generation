from pydantic import BaseModel,Field

class JobDescription(BaseModel):
    title : str
    description : str
    skills : str

class CandidateScore(BaseModel):
    id : int = Field("ID of the candidate")
    score : int = Field("Score of the candidate")
    reason : str = Field("Reason for the score you assigned")


class Candidate(BaseModel):
    id: str
    name : str
    bio : str
    email : str
    skills : str

class ScoredCandidates(BaseModel):
    id: str
    name : str
    bio : str
    email : str
    skills : str
    score : int
    reason : str    
