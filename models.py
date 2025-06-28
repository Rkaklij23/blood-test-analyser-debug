from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///results.db")
SessionLocal = sessionmaker(bind=engine)

class AnalysisResult(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    query = Column(String)
    file_path = Column(String)
    result = Column(Text)

Base.metadata.create_all(bind=engine)
