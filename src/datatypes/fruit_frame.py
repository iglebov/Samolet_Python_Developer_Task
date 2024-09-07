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
        self.db = DBworker(st)
        # self.data = pd.DataFrame(
        #     columns=["День недели", "Название дерева", "Кол-во фруктов"],
        #     data=[],
        # )
        self.data = None

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
        # TODO: Проверка валидации данных (тот же день + плод) | Работа с DataFrame
        # TODO: Обновляем одну строку в БД (Update)
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
        updated_data = pd.concat(
            [self.data, pd.DataFrame([series], columns=series.index)]
        )
        # TODO: Добавляем одну строку в БД (INSERT)
        self.db.insert_row(...)
        #
        self.data = updated_data.sort_values(
            by="День недели", key=lambda day: DAYS_SERIES[day]
        )

    def change(self) -> None:
        changed_data = self.st.data_editor(
            self.data, hide_index=True, use_container_width=True
        )
        # Валидация
        # Если не ок, то выводим ошибку

        # Если ок, то сравниваем DataFrames и UPDATE БД
        # self.data.compare(changed_data)
        # Определяем столбец для обновления, Определяем два других столбца и значения
        # TODO: Добавляем одну строку в БД (INSERT)
        self.db.update_row(...)
        # Вносим обновлённые данные
        ###
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
        self.db.delete_data()
