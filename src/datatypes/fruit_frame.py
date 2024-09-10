import random
import re

import pandas as pd
import plotly.express as px
import streamlit

from src.constants import COLUMNS, COLUMNS_LIST, DAYS_SERIES, DAYS_TUPLE, TREES
from src.database.db_worker import DBworker
from src.dynamic_filters import DynamicFilters
from src.weather.weather_parser import WeatherParser


class FruitFrame:
    def __init__(self):
        self.db = DBworker()
        self.data = self.db.select()

    def form(self, st: streamlit) -> None:
        with st.form(key="fruits_info"):
            day_name = st.radio(
                "День недели",
                *[DAYS_TUPLE],
            )
            tree_name = st.text_input(label="Название дерева (Например: Яблоня)")
            fruits_number = st.number_input(label="Число плодов (Например: 1)", step=1)

            submit_form = st.form_submit_button(label="Добавить информацию")
            if submit_form:
                if fruits_number is None or fruits_number < 0:
                    st.warning("Пожалуйста, укажите неотрицательное число плодов!")
                elif not tree_name.strip():
                    st.warning("Пожалуйста, укажите корректное название дерева.")
                elif re.findall(r"\d", tree_name):
                    st.warning("Пожалуйста, укажите название дерева без цифр.")
                else:
                    fruit_info = pd.Series(
                        {
                            "День недели": day_name,
                            "Название дерева": tree_name.strip(),
                            "Кол-во фруктов": fruits_number,
                            "Средняя температура": WeatherParser.get_weather()[
                                day_name
                            ],
                        }
                    )
                    self.insert(fruit_info)
                    st.success("Информация успешно добавлена!")

    def insert(self, fruit_info: pd.Series) -> None:
        similar_row = self.db.select_row(fruit_info)
        if not similar_row.empty:
            self.db.update(
                update_column="fruits_number",
                new_value=fruit_info["Кол-во фруктов"],
                column_1="day",
                value_1=fruit_info["День недели"],
                column_2="tree_name",
                value_2=fruit_info["Название дерева"],
                column_3="temperature",
                value_3=similar_row["Средняя температура"][0].item(),
            )
            self.data = self.db.select().sort_values(
                by="День недели", key=lambda day: DAYS_SERIES[day]
            )
        else:
            self.db.insert(fruit_info)
            updated_data = pd.concat(
                [self.data, pd.DataFrame([fruit_info], columns=fruit_info.index)]
            )
            self.data = updated_data.sort_values(
                by="День недели", key=lambda day: DAYS_SERIES[day]
            )

    def change(self, st: streamlit) -> None:
        obj = st.empty()
        obj.data_editor(
            self.data, key="editor_key", hide_index=True, use_container_width=True
        )
        if st.session_state["editor_key"]["edited_rows"]:
            if self._data_validated(st):
                data_for_update = self._get_data_for_update(st)
                self.db.update(*data_for_update)
                st.success("Изменения внесены успешно!")
            else:
                obj.empty()
                del st.session_state["editor_key"]

    def output(self) -> None:
        self.data = self.db.select().sort_values(
            by="День недели", key=lambda day: DAYS_SERIES[day]
        )
        df = DynamicFilters(self.data, filters=COLUMNS_LIST)
        df.display_filters(select=False)
        df.display_df(hide_index=True, use_container_width=True)

    def plot(self, st: streamlit) -> None:
        self.data = self.db.select().sort_values(
            by="День недели", key=lambda day: DAYS_SERIES[day]
        )
        fig = px.line(
            self.data, x="День недели", y="Кол-во фруктов", color="Название дерева"
        )
        st.plotly_chart(fig, use_container_width=True)

    def random(self) -> None:
        for day in DAYS_TUPLE:
            self.insert(
                pd.Series(
                    {
                        "День недели": day,
                        "Название дерева": random.choice(TREES),
                        "Кол-во фруктов": random.randrange(0, 50),
                        "Средняя температура": WeatherParser.get_weather()[day],
                    }
                )
            )

    def clear(self) -> None:
        self.data = self.data[0:0]
        self.db.clear()

    @staticmethod
    def _data_validated(st: streamlit) -> bool:
        edit_info = st.session_state["editor_key"]["edited_rows"]
        row = tuple(edit_info)[0]
        column = tuple(edit_info[row])[0]
        value = edit_info[row][column]

        if column == "День недели" and value not in DAYS_TUPLE:
            st.warning("Пожалуйста, укажите корректный день недели.")
            return False
        elif column == "Кол-во фруктов" and value < 0:
            st.warning("Пожалуйста, укажите неотрицательное количество плодов.")
            return False
        elif column == "Название дерева":
            if not value.strip():
                st.warning("Пожалуйста, укажите корректное название дерева.")
                return False
            elif re.findall(r"\d", value):
                st.warning("Пожалуйста, укажите название дерева без цифр.")
                return False
        elif column == "Средняя температура":
            edit_info[row][column] = float(value)
        return True

    def _get_data_for_update(self, st: streamlit) -> tuple:
        edit_info = st.session_state["editor_key"]["edited_rows"]
        update_row = tuple(edit_info)[0]
        update_column = tuple(edit_info[update_row])[0]
        new_value = edit_info[update_row][update_column]
        column_1, column_2, column_3 = [
            column for column in COLUMNS_LIST if column != update_column
        ]
        value_1 = self.data.iloc[update_row][column_1]
        value_2 = self.data.iloc[update_row][column_2]
        value_3 = self.data.iloc[update_row][column_3]
        return (
            COLUMNS[update_column],
            new_value,
            COLUMNS[column_1],
            value_1,
            COLUMNS[column_2],
            value_2,
            COLUMNS[column_3],
            value_3,
        )
