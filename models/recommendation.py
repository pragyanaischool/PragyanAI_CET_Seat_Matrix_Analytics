"""
models/recommendation.py

Recommendation Models
"""

from typing import List
from typing import Optional

from pydantic import BaseModel


class RecommendedCollege(BaseModel):

    college_name: str

    district: Optional[str] = None

    branch: Optional[str] = None

    confidence_score: float

    reason: str


class RecommendationResponse(BaseModel):

    student_rank: int

    preferred_branch: Optional[str] = None

    preferred_district: Optional[str] = None

    category: str

    recommendations: List[
        RecommendedCollege
    ]


class RankPrediction(BaseModel):

    rank: int

    category: str

    probability: float


class CollegeComparison(BaseModel):

    college_1: str

    college_2: str

    seats_1: int

    seats_2: int

    branches_1: int

    branches_2: int

    winner: str


class AIRecommendationReport(
    BaseModel
):

    student_rank: int

    branch: str

    district: str

    summary: str

    dream_colleges: List[str]

    moderate_colleges: List[str]

    safe_colleges: List[str]
