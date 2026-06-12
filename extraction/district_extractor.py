"""
extraction/district_extractor.py

District Detection Logic
"""

import re


class DistrictExtractor:

    DISTRICTS = [

        "Bangalore Urban",
        "Bangalore Rural",
        "Mysore",
        "Belagavi",
        "Dharwad",
        "Kalaburagi",
        "Bidar",
        "Raichur",
        "Ballari",
        "Vijayapura",
        "Tumakuru",
        "Shivamogga",
        "Udupi",
        "Dakshina Kannada",
        "Kodagu",
        "Chikkamagaluru",
        "Hassan",
        "Mandya",
        "Kolar",
        "Chitradurga",
        "Davanagere"
    ]

    def extract_from_address(
        self,
        address
    ):

        if not address:

            return None

        address = str(
            address
        ).lower()

        for district in self.DISTRICTS:

            if district.lower() in address:

                return district

        return None

    def assign_district(
        self,
        df
    ):

        if "address" not in df.columns:

            return df

        df["district"] = df[
            "address"
        ].apply(
            self.extract_from_address
        )

        return df
