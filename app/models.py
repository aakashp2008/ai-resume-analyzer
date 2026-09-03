from typing import List

from pydantic import BaseModel


class AnalysisResponse(BaseModel):
    filename: str
    ats_style_score: float
    skill_match_score: float
    keyword_score: float
    resume_skills: List[str]
    required_skills: List[str]
    matched_skills: List[str]
    missing_skills: List[str]
    detected_experience: List[str]
    detected_education: List[str]
    recommendations: List[str]
