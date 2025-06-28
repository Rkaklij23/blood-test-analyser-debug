import os
from dotenv import load_dotenv
load_dotenv()

from langchain.document_loaders import PDFLoader
from crewai_tools import tools
from crewai_tools.tools.serper_dev_tool import SerperDevTool

search_tool = SerperDevTool()

class BloodTestReportTool:
    @staticmethod
    async def read_data_tool(path='data/sample.pdf'):
        docs = PDFLoader(file_path=path).load()
        full_report = ""
        for data in docs:
            content = data.page_content
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"
        return full_report

class NutritionTool:
    @staticmethod
    async def analyze_nutrition_tool(blood_report_data):
        processed_data = blood_report_data
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
        return "Nutrition analysis functionality to be implemented"

class ExerciseTool:
    @staticmethod
    async def create_exercise_plan_tool(blood_report_data):
        return "Exercise planning functionality to be implemented"