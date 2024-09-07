import random
import time

import pandas as pd
import plotly.express as px
import streamlit

from src.constants import DAYS_LIST, DAYS_SERIES, DEFAULT_SLEEP_TIME, TREES
from src.dynamic_filters import DynamicFilters


class FruitFrame:
    def __init__(self, st: streamlit):
        self.st = st
        self.data = pd.DataFrame(
            columns=["День недели", "Название дерева", "Кол-во фруктов"],
            data=[],
        )

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
                if fruits_number is None or fruits_number < -1:
                    self.st.warning("Пожалуйста, укажите число плодов 0 и больше!")
                elif tree_name:
                    series = pd.Series(
                        {
                            "День недели": day_name,
                            "Название дерева": tree_name,
                            "Кол-во фруктов": fruits_number,
                        }
                    )
                    self.insert(series)
                    success = self.st.success("Информация успешно добавлена!")
                    time.sleep(DEFAULT_SLEEP_TIME)
                    success.empty()
                else:
                    warning = self.st.warning("Пожалуйста, заполните все поля.")
                    time.sleep(DEFAULT_SLEEP_TIME)
                    warning.empty()

    def insert(self, series: pd.Series) -> None:
        updated_data = pd.concat(
            [self.data, pd.DataFrame([series], columns=series.index)]
        )
        self.data = updated_data.sort_values(
            by="День недели", key=lambda day: DAYS_SERIES[day]
        )

    def change(self, state: streamlit) -> None:
        changed_data = state.data_editor(
            self.data, hide_index=True, use_container_width=True
        )
        self.data = changed_data.sort_values(
            by="День недели", key=lambda day: DAYS_SERIES[day]
        )

    def output(self) -> None:
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
