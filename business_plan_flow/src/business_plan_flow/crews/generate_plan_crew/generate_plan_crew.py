from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task, before_kickoff
import os
from dotenv import load_dotenv

from business_plan_flow.src.business_plan_flow.tools.CharacterCounterTool import CharacterCounterTool

from pathlib import Path

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
class GeneratePlanCrew():
    """GeneratePlanCrew crew"""

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
    def before_kickoff_function(self, inputs):
        return inputs

    @agent
    def business_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['business_designer'],
            tools=[CharacterCounterTool()],
            llm=self.llm,
            verbose=True
        )

    @agent
    def product_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['product_designer'],
            tools=[CharacterCounterTool()],
            llm=self.llm,
            verbose=True
        )

    @task
    def create_business_concept(self) -> Task:
        return Task(
            config=self.tasks_config['create_business_concept']
        )

    @task
    def create_product_design(self) -> Task:
        return Task(
            config=self.tasks_config['create_product_design'],
            context=[self.create_business_concept()]
        )
   
    @crew
    def crew(self) -> Crew:
        """Creates the GeneratePlanCrew crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True
        )
    
    def run(self, inputs: dict = None, feedback: str = None):
        try:
            if inputs is None:
                inputs = {}
            inputs['feedback'] = feedback or ""
            self.crew().kickoff(inputs=inputs)
            responses = []
            for task in self.tasks:
                task_output = task.output.raw if hasattr(task, 'output') else ""
                responses.append(task_output)
            return responses
        except Exception as e:
            raise Exception(f"Error while running the crew: {e}")
