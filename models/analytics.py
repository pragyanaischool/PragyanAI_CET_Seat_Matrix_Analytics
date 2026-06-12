"""
models/analytics.py

Analytics Models
"""

from typing import Optional

from pydantic import BaseModel


class DistrictAnalytics(BaseModel):

    district: str

    college_count: int

    branch_count: int

    total_seats: int

    average_seats: float


class BranchAnalytics(BaseModel):

    branch_name: str

    college_count: int

    total_seats: int

    average_intake: float


class CollegeAnalytics(BaseModel):

    college_name: str

    district: str

    total_branches: int

    total_seats: int

    rank: Optional[int] = None


class GrowthAnalytics(BaseModel):

    college_name: str

    start_year: int

    end_year: int

    start_seats: int

    end_seats: int

    growth_percentage: float


class DashboardMetrics(BaseModel):

    total_colleges: int

    total_branches: int

    total_districts: int

    total_seats: int

    year: int
