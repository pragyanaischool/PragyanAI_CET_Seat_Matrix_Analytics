"""
exports/report_generator.py

AI Report Generator
"""

from datetime import datetime

import pandas as pd

from exports.pdf_export import (
    PDFExporter
)

from exports.excel_export import (
    ExcelExporter
)


class ReportGenerator:

    def __init__(self):

        self.pdf_exporter = (
            PDFExporter()
        )

        self.excel_exporter = (
            ExcelExporter()
        )

    def generate_summary_report(
        self,
        df
    ):

        total_colleges = (
            df["college_name"]
            .nunique()
        )

        total_seats = (
            df["total_intake"]
            .sum()
        )

        total_branches = (
            df["course_name"]
            .nunique()
        )

        report = f"""
        Karnataka CET College Analytics

        Total Colleges:
        {total_colleges}

        Total Seats:
        {total_seats}

        Total Branches:
        {total_branches}
        """

        return report

    def generate_top_colleges(
        self,
        df,
        top_n=10
    ):

        return (
            df.groupby(
                "college_name"
            )["total_intake"]
            .sum()
            .sort_values(
                ascending=False
            )
            .head(top_n)
            .reset_index()
        )

    def generate_district_report(
        self,
        df
    ):

        return (
            df.groupby(
                "district"
            )["total_intake"]
            .sum()
            .reset_index()
        )

    def export_excel_report(
        self,
        df,
        filepath
    ):

        college_df = (
            self.generate_top_colleges(
                df
            )
        )

        district_df = (
            self.generate_district_report(
                df
            )
        )

        branch_df = (
            df.groupby(
                "course_name"
            )["total_intake"]
            .sum()
            .reset_index()
        )

        return self.excel_exporter.export_analytics(
            college_df,
            district_df,
            branch_df,
            filepath
        )

    def export_pdf_report(
        self,
        df,
        filepath
    ):

        summary = (
            self.generate_summary_report(
                df
            )
        )

        return (
            self.pdf_exporter
            .create_pdf(
                "CET College Intelligence Report",
                summary,
                filepath
            )
        )

    def generate_college_report(
        self,
        college_name,
        college_info,
        filepath
    ):

        summary = f"""
        College Name:
        {college_name}

        District:
        {college_info.get('district')}

        NAAC Grade:
        {college_info.get('naac_grade')}

        Placement:
        {college_info.get('placement_rate')}

        AI Summary:
        {college_info.get('summary')}
        """

        return (
            self.pdf_exporter
            .create_college_report(
                college_name,
                summary,
                filepath
            )
        )

    def generate_comparison_report(
        self,
        college1,
        college2,
        comparison_df,
        filepath
    ):

        summary = f"""
        College Comparison

        College A:
        {college1}

        College B:
        {college2}

        Total Compared Branches:
        {len(comparison_df)}

        Generated:
        {datetime.now()}
        """

        return (
            self.pdf_exporter
            .create_pdf(
                "College Comparison Report",
                summary,
                filepath
            )
        )
      
