from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Float, DateTime, func
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    compensation = Column(Float, nullable=False)
    
    # Default to not assigned
    assigned = Column(Boolean, default=False)
    
    # Foreign keys
    business_id = Column(Integer, ForeignKey("businesses.id"), nullable=False)
    assigned_society_id = Column(Integer, ForeignKey("societies.id"), nullable=True)
    
    # Relationships
    business = relationship("Business", backref="projects")
    assigned_society = relationship("Society", foreign_keys=[assigned_society_id])
    
    # This will give access to all societies that applied for this project
    applying_societies = relationship(
        "Society",
        secondary="project_applications",
        backref="applied_projects"
    )
    
    # Project status
    status = Column(String(50), default="open", nullable=False)  # open, in_progress, completed, cancelled
    created_at = Column(DateTime, server_default=func.now())
    deadline = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)


class ProjectApplication(Base):
    __tablename__ = "project_applications"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    society_id = Column(Integer, ForeignKey("societies.id"), nullable=False)
    
    # You could add additional fields here like:
    application_date = Column(String, nullable=True)  # Could use DateTime with timezone
    notes = Column(Text, nullable=True)
    proposed_timeline = Column(String, nullable=True)
    
    status = Column(String(50), default="pending", nullable=False)  # pending, accepted, rejected
    budget_proposal = Column(Float, nullable=True)
    estimated_completion_time = Column(Integer, nullable=True)  # In days

    