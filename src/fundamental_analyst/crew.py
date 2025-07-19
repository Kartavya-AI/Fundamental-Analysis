from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from .tools.serper_tool import serper_tool


@CrewBase
class FundamentalAnalyst():
    """FundamentalAnalyst crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def company_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['company_researcher'],
            tools=[serper_tool],
            verbose=True)

    @agent
    def financial_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_analyst'],
            tools=[serper_tool], 
            verbose=True)

    @agent
    def valuation_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['valuation_analyst'], 
            tools=[serper_tool],
            verbose=True)

    @agent
    def macro_sector_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['macro_sector_analyst'], 
            tools=[serper_tool],
            verbose=True)

    @agent
    def risk_sentiment_analyst(self) -> Agent:
        return Agent(config=self.agents_config['risk_sentiment_analyst'], verbose=True)

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(config=self.agents_config['reporting_analyst'], verbose=True)

    @task
    def company_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['company_research_task'],
            output_file="company_research_task.md")

    @task
    def financial_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['financial_analysis_task'],
            context=[self.company_research_task()],
            output_file="financial_analysis_task.md")

    @task
    def valuation_task(self) -> Task:
        return Task(
            config=self.tasks_config['valuation_task'],
            context=[self.company_research_task(),self.financial_analysis_task()],
            output_file="valuation_task.md")

    @task
    def macro_sector_task(self) -> Task:
        return Task(
            config=self.tasks_config['macro_sector_task'],
            output_file="macro_sector_task.md")

    @task
    def risk_sentiment_task(self) -> Task:
        return Task(
            config=self.tasks_config['risk_sentiment_task'],
            context=[
                self.company_research_task(),
                self.financial_analysis_task(),
                self.valuation_task(),
                self.macro_sector_task(),
            ],
            output_file="risk_sentiment_task.md")

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            context=[
                self.company_research_task(),
                self.financial_analysis_task(),
                self.valuation_task(),
                self.macro_sector_task(),
                self.risk_sentiment_task(),
            ],
            output_file='report.md')

    @crew
    def crew(self) -> Crew:
        """Creates the FundamentalAnalyst crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
