#!/usr/bin/env python
import os
import google.generativeai as genai
from typing import Optional, List, Dict
from dotenv import load_dotenv
from pydantic import BaseModel

from crewai.flow import Flow, listen, start, router

from .crews.generate_plan_crew.generate_plan_crew import GeneratePlanCrew
from .crews.review_plan_crew.review_plan_crew import ReviewPlanCrew

class BusinessPlanState(BaseModel):
    user_inputs: Dict = {}
    business_plan: List[str] = []
    feedback: Optional[str] = None
    valid: bool = False
    retry_count: int = 0

class BusinessPlanFlow(Flow[BusinessPlanState]):

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)

    @start("retry")
    def generate_business_plan(self):
        crew = GeneratePlanCrew()
        result = crew.run(inputs=self.state.user_inputs, feedback=self.state.feedback)
        self.state.business_plan = result
        
    @router(generate_business_plan)
    def evaluate_business_plan(self):
        if self.state.retry_count == 1:
            return "completed"
        crew = ReviewPlanCrew()
        result = crew.run(input={"business_plan": "\n\n".join(self.state.business_plan)})
        self.state.feedback = result
        self.state.retry_count += 1

        return "retry"

    @listen("completed")
    def save_business_plan(self):
        return self.state
