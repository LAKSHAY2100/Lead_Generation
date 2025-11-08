from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from lead_score_flow.types import CandidateScore

@CrewBase
class LeadScoreCrew():
    @agent
    def hr_evaluation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["hr_evaluation_agent"],
            verbose = True
        )
    
    @task
    def evaluate_candidate()-> Task:
        return Task(
            config=self.tasks_config['evaluate_candidate'],
            verbose=True
        )
    
    
