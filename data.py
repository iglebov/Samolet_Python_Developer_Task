import pandas as pd
import streamlit as st
from streamlit_dynamic_filters import DynamicFilters

fruit_data = pd.DataFrame(
    columns=["День недели", "Название дерева", "Кол-во фруктов"],
    data=[["Понедельник", "Яблоня", 2], ["Вторник", "Вишня", 3]],
)


def update_fruit_data(df: pd.DataFrame) -> None:
    global fruit_data

    fruit_data = df


df_with_filters = DynamicFilters(
    fruit_data, filters=["День недели", "Название дерева", "Кол-во фруктов"]
)


def display_table() -> None:
    st.session_state.clicked = True
