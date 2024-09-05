import random
import time

import altair as alt
import pandas as pd
import streamlit

from constants import DAYS_LIST, DAYS_SERIES, DEFAULT_SLEEP_TIME, TREES
from dynamic_filters import DynamicFilters


class FruitFrame:
    def __init__(self):
        self.data = pd.DataFrame(
            columns=["День недели", "Название дерева", "Кол-во фруктов"],
            data=[],
        )

    def form(self, st: streamlit):
        with st.form(key="fruits_info"):
            day_name = st.radio(
                "День недели",
                *[DAYS_LIST],
            )
            tree_name = st.text_input(label="Название дерева (Например: Яблоня)")
            fruits_number = st.number_input(label="Число плодов (Например: 1)", step=1)

            submit_form = st.form_submit_button(label="Добавить информацию")
            if submit_form:
                if fruits_number is None or fruits_number < -1:
                    st.warning("Пожалуйста, укажите число плодов 0 и больше!")
                elif tree_name:
                    series = pd.Series(
                        {
                            "День недели": day_name,
                            "Название дерева": tree_name,
                            "Кол-во фруктов": fruits_number,
                        }
                    )
                    self.insert(series)
                    success = st.success("Информация успешно добавлена!")
                    time.sleep(DEFAULT_SLEEP_TIME)
                    success.empty()
                else:
                    warning = st.warning("Пожалуйста, заполните все поля.")
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

    def plot(self, state: streamlit) -> None:
        state.write(
            alt.Chart(self.data)
            .mark_bar()
            .encode(
                x=alt.X("День недели", sort=None, title="День недели"),
                y=alt.Y("Кол-во фруктов", title="Кол-во фруктов"),
                color="Название дерева",
            ),
            use_container_width=True,
        )

    def random(self) -> None:
        for i in range(10):
            self.insert(
                pd.Series(
                    {
                        "День недели": random.choice(DAYS_LIST),
                        "Название дерева": random.choice(TREES),
                        "Кол-во фруктов": random.randrange(0, 50),
                    }
                )
            )

    def clear(self) -> None:
        self.data = self.data[0:0]
