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
    def evaluate_candidate(self)-> Task:
        return Task(
            config=self.tasks_config['evaluate_candidate'],
            output_pydantic=CandidateScore,
            verbose=True
        )
    
    
    @crew
    def crew(self):
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )

