import random
import time

import pandas as pd
import plotly.express as px
import streamlit

from src.constants import DAYS_LIST, DAYS_SERIES, DEFAULT_SLEEP_TIME, TREES
from src.database.db_worker import DBworker
from src.dynamic_filters import DynamicFilters


class FruitFrame:
    def __init__(self, st: streamlit):
        self.st = st
        self.db = DBworker()
        self.data = self.db.select()

    def form(self) -> None:
        with self.st.form(key="fruits_info"):
            day_name = self.st.radio(
                "День недели",
                *[DAYS_LIST],
            )
            tree_name = self.st.text_input(label="Название дерева (Например: Яблоня)")
            fruits_number = self.st.number_input(
                label="Число плодов (Например: 1)", step=1
            )

            submit_form = self.st.form_submit_button(label="Добавить информацию")
            if submit_form:
                if fruits_number is None or fruits_number < 0:
                    self.st.warning("Пожалуйста, укажите неотрицательное число плодов!")
                elif tree_name:
                    fruit_info = pd.Series(
                        {
                            "День недели": day_name,
                            "Название дерева": tree_name,
                            "Кол-во фруктов": fruits_number,
                        }
                    )
                    self.insert(fruit_info)

                    success = self.st.success("Информация успешно добавлена!")
                    time.sleep(DEFAULT_SLEEP_TIME)
                    success.empty()
                else:
                    warning = self.st.warning("Пожалуйста, заполните все поля.")
                    time.sleep(DEFAULT_SLEEP_TIME)
                    warning.empty()

    def insert(self, fruit_info: pd.Series) -> None:
        self.db.insert(fruit_info)
        updated_data = pd.concat(
            [self.data, pd.DataFrame([fruit_info], columns=fruit_info.index)]
        )
        self.data = updated_data.sort_values(
            by="День недели", key=lambda day: DAYS_SERIES[day]
        )

    def change(self) -> None:
        changed_data = self.st.data_editor(
            self.data, hide_index=True, use_container_width=True
        )
        if self._data_validated(changed_data):
            self.db.update(...)
            self.data = changed_data.sort_values(
                by="День недели", key=lambda day: DAYS_SERIES[day]
            )
        else:
            self.st.warning("...")

    def output(self) -> None:
        self.data = self.db.select().sort_values(
            by="День недели", key=lambda day: DAYS_SERIES[day]
        )
        df = DynamicFilters(
            self.data, filters=["День недели", "Название дерева", "Кол-во фруктов"]
        )
        df.display_filters(select=False)
        df.display_df(hide_index=True, use_container_width=True)

    def plot(self) -> None:
        fig = px.line(
            self.data, x="День недели", y="Кол-во фруктов", color="Название дерева"
        )
        self.st.plotly_chart(fig, use_container_width=True)

    def random(self) -> None:
        for day in DAYS_LIST:
            self.insert(
                pd.Series(
                    {
                        "День недели": day,
                        "Название дерева": random.choice(TREES),
                        "Кол-во фруктов": random.randrange(0, 50),
                    }
                )
            )

    def clear(self) -> None:
        self.data = self.data[0:0]
        self.db.clear()

    def _data_validated(self, changed_data: pd.DataFrame) -> bool:
        compared_df = self.data.compare(changed_data)
        row = compared_df.index.values[0].item()
        column = compared_df.columns[0][0]
        value = changed_data[column][row]

        if column == "День недели" and value not in DAYS_LIST:
            self.st.warning("Пожалуйста, укажите корректный день недели.")
            return False
        return True

        # Если уже существует, то обновляем количество плодов
        # if (
        #     (self.data["День недели"] == series["День недели"])
        #     and (self.data["Название дерева"] == series["Название дерева"])
        # ).any():
        #     row_index = self.data.index[
        #         self.data["День недели"] == "David"
        #         and self.data["Название дерева"] == "..."
        #     ].tolist()
        #     self.data.iloc[row_index]["Кол-во плодов"] = series["Кол-во плодов"]
        # Если не существует, то просто добавляем
        # else:
