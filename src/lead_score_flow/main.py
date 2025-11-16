import asyncio
from typing import List

from crewai.flow.flow import Flow,listen,or_,router
from pydantic import BaseModel

from lead_score_flow.types import Candidate ,CandidateScore , ScoredCandidate
from lead_score_flow.constants import JOB_DESCRIPTION
from lead_score_flow.crews.lead_response_crew import lead_response_crew
from lead_score_flow.crews.lead_score_crew import lead_score_crew
from lead_score_flow.utlis.candidates