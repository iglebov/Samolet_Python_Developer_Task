from typing import Any, Dict, Union


class DBworker:
    def __init__(self, st):
        self.connection = st.connection("postgresql", type="sql")

    def insert_row(self, fruit_info: Dict[str, Union[str, list]]) -> None:
        insert_query = f"""INSERT INTO fruits_info (day, tree_name, fruits_number)
                                VALUES
                                (
                                {fruit_info.get("day")},
                                {fruit_info.get("tree_name")},
                                {fruit_info.get("fruits_number")}
                                );"""
        self.connection.query(insert_query, ttl="10m")
        self.connection.commit()

    def update_row(
        self,
        update_column: str,
        new_value: Any,
        column_1: str,
        value_1,
        column_2,
        value_2,
    ) -> None:
        update_query = f"""UPDATE fruits_info
                           SET {update_column} = {new_value}
                           WHERE {column_1} = {value_1} AND {column_2} = {value_2};"""
        self.connection.query(update_query, ttl="10m")
        self.connection.commit()

    def delete_data(self):
        self.connection.query("TRUNCATE fruits_info", ttl="10m")
        self.connection.commit()

    def finish(self):
        self.connection.close()
