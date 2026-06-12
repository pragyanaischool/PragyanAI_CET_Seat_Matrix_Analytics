"""
extraction/table_extractor.py

Extract Tables From PDF
"""

import camelot
import pandas as pd


class TableExtractor:

    def __init__(self):
        pass

    def extract_tables(
        self,
        pdf_path
    ):

        tables = camelot.read_pdf(
            pdf_path,
            pages="all",
            flavor="stream"
        )

        return tables

    def tables_to_dataframe(
        self,
        pdf_path
    ):

        tables = self.extract_tables(
            pdf_path
        )

        dfs = []

        for table in tables:

            dfs.append(
                table.df
            )

        if dfs:

            return pd.concat(
                dfs,
                ignore_index=True
            )

        return pd.DataFrame()

    def save_tables(
        self,
        pdf_path,
        output_csv
    ):

        df = self.tables_to_dataframe(
            pdf_path
        )

        df.to_csv(
            output_csv,
            index=False
        )

        return output_csv
