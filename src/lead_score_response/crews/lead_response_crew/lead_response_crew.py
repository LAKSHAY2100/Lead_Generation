from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class lead_response():

    @agent
    def lead_response_agent(self):
        return Agent(
            config = self.agents_config['email_followup_agent'],
            verbose=True
        )
    
    @task   
    def lead_response_task(self):
        return Task(
            config = self.tasks_config['send_followup_email'],
            verbose=True
        )
    
    @crew
    def crew(self):
        return Crew(
            agents=self.agents,
            task=self.tasks,
            process=Process.sequential,
            verbose=True
        )