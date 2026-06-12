"""
models/seat_matrix.py

Seat Matrix Record Model
"""

from typing import Optional

from pydantic import BaseModel


class SeatMatrixRecord(BaseModel):

    year: int

    college_code: str

    college_name: str

    district: Optional[str] = None

    course_code: Optional[str] = None

    course_name: str

    total_intake: int

    kea_seats: int = 0

    hk_seats: int = 0

    rk_seats: int = 0

    management_seats: int = 0

    govt_seats: int = 0

    category: Optional[str] = None

    def to_dict(self):

        return self.model_dump()


class SeatMatrixBatch(BaseModel):

    year: int

    records: list[SeatMatrixRecord]

    total_colleges: int = 0

    total_branches: int = 0

    total_seats: int = 0

    def summary(self):

        return {

            "year":
                self.year,

            "records":
                len(self.records),

            "total_colleges":
                self.total_colleges,

            "total_branches":
                self.total_branches,

            "total_seats":
                self.total_seats
        }
