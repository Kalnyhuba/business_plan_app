#!/usr/bin/env python
import os
import google.generativeai as genai
from typing import Optional, List, Dict
from dotenv import load_dotenv
from pydantic import BaseModel

from crewai.flow import Flow, listen, start, router

from .crews.generate_plan_crew.generate_plan_crew import GeneratePlanCrew

class BusinessPlanState(BaseModel):
    user_inputs: Dict = {}
    business_plan: str = ""

class BusinessPlanFlow(Flow[BusinessPlanState]):
    @start("done")
    async def generate_business_plan(self):
        crew = GeneratePlanCrew()
        result = crew.run(inputs=self.state.user_inputs)
        self.state.business_plan = result
        return self.state

    @listen("done")
    def done(self):
        return self.state
