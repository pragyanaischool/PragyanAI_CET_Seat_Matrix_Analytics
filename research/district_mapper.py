"""
research/district_mapper.py

District Mapping Utility
"""


class DistrictMapper:

    DISTRICT_MAPPING = {

        "RV College of Engineering":
            "Bangalore Urban",

        "BMS College of Engineering":
            "Bangalore Urban",

        "PES University":
            "Bangalore Urban",

        "NIE Mysore":
            "Mysore",

        "SJCE Mysore":
            "Mysore"
    }

    def get_district(
        self,
        college_name
    ):

        return self.DISTRICT_MAPPING.get(
            college_name,
            "Unknown"
        )

    def update_mapping(
        self,
        college_name,
        district
    ):

        self.DISTRICT_MAPPING[
            college_name
        ] = district

    def district_summary(
        self,
        college_name
    ):

        return {

            "college":
                college_name,

            "district":
                self.get_district(
                    college_name
                )
        }
