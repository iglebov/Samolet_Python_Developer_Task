from typing import Any

import pandas as pd
import psycopg2
import streamlit as st
from pandas import DataFrame


class DBworker:
    def __init__(self):
        self.connection = psycopg2.connect(
            user=st.secrets["username"],
            host=st.secrets["host"],
            port=st.secrets["port"],
            password=st.secrets["password"],
            database=st.secrets["database"],
        )

    def select(self) -> pd.DataFrame:
        return pd.read_sql("SELECT * FROM fruits_info", self.connection).rename(
            columns={
                "day": "День недели",
                "tree_name": "Название дерева",
                "fruits_number": "Кол-во фруктов",
                "temperature": "Средняя температура",
            }
        )

    def select_row(self, fruit_info: pd.Series) -> DataFrame:
        return pd.read_sql(
            f"SELECT * FROM fruits_info WHERE day = '{fruit_info["День недели"]}' "
            f"AND tree_name = '{fruit_info["Название дерева"]}'",
            self.connection,
        ).rename(
            columns={
                "day": "День недели",
                "tree_name": "Название дерева",
                "fruits_number": "Кол-во фруктов",
                "temperature": "Средняя температура",
            }
        )

    def insert(self, fruit_info: pd.Series) -> None:
        insert_query = f"""INSERT INTO fruits_info (day, tree_name, fruits_number, temperature) VALUES
            ('{fruit_info["День недели"]}', '{fruit_info["Название дерева"]}',
            {fruit_info["Кол-во фруктов"]}, {fruit_info["Средняя температура"]});"""
        cursor = self.connection.cursor()
        cursor.execute(insert_query)
        self.connection.commit()

    def update(
        self,
        update_column: str,
        new_value: Any,
        column_1: str,
        value_1: str | int | float,
        column_2: str,
        value_2: str | int | float,
        column_3: str,
        value_3: str | int | float,
    ) -> None:
        update_query = f"""UPDATE fruits_info SET {update_column} = {self._get_value(new_value)}
                           WHERE {column_1} = {self._get_value(value_1)} AND {column_2} = {self._get_value(value_2)}
                           AND {column_3} = {self._get_value(value_3)};"""
        cursor = self.connection.cursor()
        cursor.execute(update_query)
        self.connection.commit()

    def update_duplicate(
        self,
        fruits_value: int,
        temperature_value: float,
        day_value: str,
        tree_value: str,
    ) -> None:
        update_query = f"""UPDATE fruits_info SET fruits_number = {fruits_value}, temperature = {temperature_value}
                           WHERE day = '{day_value}' AND tree_name = '{tree_value}';"""
        cursor = self.connection.cursor()
        cursor.execute(update_query)
        self.connection.commit()

    @staticmethod
    def _get_value(value: str | int | float) -> str:
        if isinstance(value, (int, float)):
            return f"{value}"
        else:
            return f"'{value}'"

    def clear(self):
        cursor = self.connection.cursor()
        cursor.execute("TRUNCATE fruits_info")
        self.connection.commit()
