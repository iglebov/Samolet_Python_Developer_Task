from typing import Any

import pandas as pd
import psycopg2
import streamlit as st


class DBworker:
    def __init__(
        self,
    ):
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

    def insert(self, fruit_info: pd.Series) -> None:
        insert_query = (
            f"""INSERT INTO fruits_info (day, tree_name, fruits_number, temperature) VALUES """
            f"""('{fruit_info["День недели"]}', '{fruit_info["Название дерева"]}',  """
            f"""{fruit_info["Кол-во фруктов"]}, {fruit_info["Средняя температура"]});"""
        )
        cursor = self.connection.cursor()
        cursor.execute(insert_query)
        self.connection.commit()

    def update(
        self,
        update_column: str,
        new_value: Any,
        column_1: str,
        value_1: str | int,
        column_2: str,
        value_2: str | int,
    ) -> None:
        update_query = f"""UPDATE fruits_info SET {update_column} = '{new_value}'
        WHERE {column_1} = '{value_1}' AND {column_2} = '{value_2}';"""
        cursor = self.connection.cursor()
        cursor.execute(update_query)
        self.connection.commit()

    def clear(self):
        cursor = self.connection.cursor()
        cursor.execute("TRUNCATE fruits_info")
        self.connection.commit()
