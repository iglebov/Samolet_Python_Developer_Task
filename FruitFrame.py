import pandas as pd
import streamlit
from streamlit_dynamic_filters import DynamicFilters


class FruitFrame:
    def __init__(self):
        self.data = pd.DataFrame(
            columns=["День недели", "Название дерева", "Кол-во фруктов"], data=[]
        )

    def insert(self, row: pd.Series) -> None:
        self.data = pd.concat([self.data, pd.DataFrame([row], columns=row.index)])

    def change(self, state: streamlit) -> None:
        self.data = state.data_editor(self.data)

    def output(self) -> None:
        df = DynamicFilters(
            self.data, filters=["День недели", "Название дерева", "Кол-во фруктов"]
        )
        df.display_filters()
        df.display_df()
