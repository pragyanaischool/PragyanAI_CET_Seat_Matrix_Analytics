"""
models/college.py

College Master Model
"""

from typing import List, Optional

from pydantic import BaseModel
from pydantic import Field


class College(BaseModel):

    college_code: str = Field(
        default=""
    )

    college_name: str

    district: Optional[str] = None

    college_type: Optional[str] = None

    address: Optional[str] = None

    website: Optional[str] = None

    nirf_rank: Optional[int] = None

    naac_grade: Optional[str] = None

    placement_rate: Optional[float] = None

    highest_package: Optional[float] = None

    average_package: Optional[float] = None

    branches: List[str] = []

    total_seats: int = 0

    established_year: Optional[int] = None

    autonomous: bool = False

    def to_dict(self):

        return self.model_dump()
