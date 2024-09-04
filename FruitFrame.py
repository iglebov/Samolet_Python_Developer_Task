import pandas as pd
import streamlit
from streamlit_dynamic_filters import DynamicFilters

days = pd.Series(
    {
        "Понедельник": 0,
        "Вторник": 1,
        "Среда": 2,
        "Четверг": 3,
        "Пятница": 4,
        "Суббота": 5,
        "Воскресенье": 6,
    }
)


class FruitFrame:
    def __init__(self):
        self.data = pd.DataFrame(
            columns=["День недели", "Название дерева", "Кол-во фруктов"],
            data=[["Вторник", "а", 1], ["Вторник", "б", 2], ["Среда", "а", 3]],
        )

    def insert(self, row: pd.Series) -> None:
        updated_data = pd.concat([self.data, pd.DataFrame([row], columns=row.index)])
        self.data = updated_data.sort_values(
            by="День недели", key=lambda day: days[day]
        )

    def change(self, state: streamlit) -> None:
        changed_data = state.data_editor(self.data, hide_index=True)
        self.data = changed_data.sort_values(
            by="День недели", key=lambda day: days[day]
        )

    def output(self) -> None:
        df = DynamicFilters(
            self.data, filters=["День недели", "Название дерева", "Кол-во фруктов"]
        )
        df.display_filters()
        df.display_df(hide_index=True)
