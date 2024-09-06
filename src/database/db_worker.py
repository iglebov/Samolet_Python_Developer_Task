from typing import Dict, Union

import psycopg2


class DBWorker:
    def __init__(self, user: str, host: str, port: str, password: str, database: str):
        self.connection = self.connect(user, host, port, password, database)

    @staticmethod
    def connect(user: str, host: str, port: str, password: str, database: str):
        st
        # st.connect(...)
        return psycopg2.connect(
            user=user, host=host, port=port, password=password, database=database
        )

    def insert_row(self, fruit_info: Dict[str, Union[str, list]]) -> None:
        postgres_insert_query = """INSERT INTO fruits (day, tree_name, fruits_number)
                                VALUES (%s, %s, %s);"""
        record_to_insert = (
            fruit_info.get("day"),
            fruit_info.get("tree_name"),
            fruit_info.get("fruits_number"),
        )
        cursor = self.connection.cursor()
        cursor.execute(postgres_insert_query, record_to_insert)
        self.connection.commit()

    def finish(self):
        self.connection.close()
