from celery import Celery
from crewai import Crew, Process
from agents import doctor, verifier, nutritionist, exercise_specialist
from task import help_patients, nutrition_analysis, exercise_planning, verification
from models import SessionLocal, AnalysisResult

celery_app = Celery("tasks", broker="redis://localhost:6379/0")

@celery_app.task
def analyze_pdf_task(query, file_path):
    crew = Crew(
        agents=[doctor, verifier, nutritionist, exercise_specialist],
        tasks=[help_patients, verification, nutrition_analysis, exercise_planning],
        process=Process.sequential,
    )
    result = crew.kickoff({"query": query})

    db = SessionLocal()
    record = AnalysisResult(query=query, file_path=file_path, result=str(result))
    db.add(record)
    db.commit()
    db.close()

    return str(result)
