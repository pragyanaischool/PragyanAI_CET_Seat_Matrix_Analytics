"""
exports/excel_export.py

Excel Export Utility
"""

import pandas as pd
from datetime import datetime


class ExcelExporter:

    def __init__(self):
        pass

    def export_dataframe(
        self,
        df,
        filepath
    ):

        with pd.ExcelWriter(
            filepath,
            engine="openpyxl"
        ) as writer:

            df.to_excel(
                writer,
                sheet_name="Data",
                index=False
            )

        return filepath

    def export_multiple_sheets(
        self,
        sheets,
        filepath
    ):
        """
        sheets = {
            "College": college_df,
            "District": district_df
        }
        """

        with pd.ExcelWriter(
            filepath,
            engine="openpyxl"
        ) as writer:

            for name, data in sheets.items():

                data.to_excel(
                    writer,
                    sheet_name=name,
                    index=False
                )

        return filepath

    def export_analytics(
        self,
        college_df,
        district_df,
        branch_df,
        filepath
    ):

        sheets = {

            "Colleges": college_df,

            "Districts": district_df,

            "Branches": branch_df
        }

        return self.export_multiple_sheets(
            sheets,
            filepath
        )
