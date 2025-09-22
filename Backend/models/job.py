from sqlalchemy import column, Integer, String, DateTime
from sqlalchemy.sql import func


from db.database import Base


class StoryJob(Base):
    __tablename__ = "story_jobs"
    
    id = column(Integer, primary_key=True, index=True)
    job_id = column(String, index=True, unique=True)
    session_id = column(String, index=True)
    theme = column(String, index=True)
    status = column(String, index= True)
    story_id = column(Integer, index=True)
    error = column(String, index= True)
    created_at = column(DateTime(timezone=True), server_default=func.now())
    completed_at = column(DateTime(timezone=True), nullable=True)
    