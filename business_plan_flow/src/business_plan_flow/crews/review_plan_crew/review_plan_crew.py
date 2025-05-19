from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, before_kickoff
import os
from dotenv import load_dotenv
from pathlib import Path

from business_plan_flow.src.business_plan_flow.tools.CharacterCounterTool import CharacterCounterTool

def load_env_from_project_root(env_filename=".env", max_depth=5) -> bool:
    """
    Recursively searches upward from the current file's path to find and load a .env file.

    Args:
        env_filename (str): Name of the env file to search for (default: ".env")
        max_depth (int): Max levels to go up the directory tree

    Returns:
        bool: True if the file was found and loaded, False otherwise
    """
    current_path = Path(__file__).resolve().parent

    for _ in range(max_depth):
        env_path = current_path / env_filename
        if env_path.exists():
            load_dotenv(dotenv_path=env_path)
            print(f"[.env loaded from] {env_path}")
            return True
        current_path = current_path.parent

    print("[.env file not found]")
    return False

load_env_from_project_root()

@CrewBase
class ReviewPlanCrew():
    """ReviewPlanCrew crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @property
    def llm(self):
        if not hasattr(self, "_llm"):
            api_key = os.environ["GEMINI_API_KEY"]
            if not api_key:
                raise ValueError("Missing GEMINI_API_KEY from environment")
            import google.generativeai as genai
            genai.configure(api_key=api_key)

            self._llm = LLM(
                model="gemini/gemini-2.5-flash-preview-04-17",
                temperature=0.3,
                reasoning_effort="high"
            )
        return self._llm

    @before_kickoff
    def before_kickoff(self, inputs):
        return inputs

    @agent
    def business_plan_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['business_plan_reviewer'],
            llm=self.llm,
            tools=[CharacterCounterTool()],
            verbose=True
        )
    
    @task
    def review_business_plan(self) -> Task:
        return Task(
            config=self.tasks_config['review_business_plan']
        )
    
    @crew
    def crew(self) -> Crew:
        """Creates the ReviewPlanCrew crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
    
    def run(self, input: dict = None):
        try:
            self.crew().kickoff(inputs=input)
            return self.tasks[0].output.raw
        except Exception as e:
            raise Exception(f"Error while running the crew: {e}")
