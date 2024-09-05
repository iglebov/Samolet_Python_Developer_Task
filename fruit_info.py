import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from constants import (
    CHANGE_BUTTON_CSS_STYLE,
    CLEAR_BUTTON_CSS_STYLE,
    INSERT_BUTTON_CSS_STYLE,
    OUTPUT_BUTTON_CSS_STYLE,
    PLOT_BUTTON_CSS_STYLE,
    RANDOM_BUTTON_CSS_STYLE,
    STATES,
)
from FruitFrame import FruitFrame

_, col, _ = st.columns([1, 4, 1])

with col:
    st.title("Информация о плодах")


if "fruit_frame" not in st.session_state:
    st.session_state["fruit_frame"] = FruitFrame()
for state in STATES:
    if state not in st.session_state:
        setattr(st.session_state, state, False)


def hide_others_states(unique_state: str) -> None:
    for state in STATES:
        if state != unique_state:
            setattr(st.session_state, state, False)


with stylable_container(
    "green",
    css_styles=INSERT_BUTTON_CSS_STYLE,
):
    insert = st.button("Ввести", on_click=lambda: hide_others_states("insert_state"))

if insert or st.session_state.insert_state:
    st.session_state.insert_state = True
    st.session_state["fruit_frame"].form(st)

with stylable_container(
    "red",
    css_styles=CHANGE_BUTTON_CSS_STYLE,
):
    change = st.button("Изменить", on_click=lambda: hide_others_states("change_state"))

if change or st.session_state.change_state:
    st.session_state.change_state = True
    st.session_state["fruit_frame"].change(st)

with stylable_container(
    "blue",
    css_styles=OUTPUT_BUTTON_CSS_STYLE,
):
    output = st.button("Вывести", on_click=lambda: hide_others_states("output_state"))

if output or st.session_state.output_state:
    st.session_state.output_state = True
    st.session_state["fruit_frame"].output()

with stylable_container(
    "orange",
    css_styles=PLOT_BUTTON_CSS_STYLE,
):
    plot = st.button("График", on_click=lambda: hide_others_states("plot_state"))

if plot or st.session_state.plot_state:
    st.session_state.plot_state = True
    st.session_state["fruit_frame"].plot(st)

with stylable_container(
    "pink",
    css_styles=RANDOM_BUTTON_CSS_STYLE,
):
    random = st.button(
        "Случайные данные", on_click=lambda: hide_others_states("random_state")
    )

if random or st.session_state.random_state:
    st.session_state.random_state = True
    st.session_state["fruit_frame"].random()
    st.success("Добавлено 10 случайных строк!")

with stylable_container(
    "dark",
    css_styles=CLEAR_BUTTON_CSS_STYLE,
):
    clear = st.button("Очистить", on_click=lambda: hide_others_states("clear_state"))

if clear or st.session_state.clear_state:
    st.session_state.clear_state = True
    st.session_state["fruit_frame"].clear()
    st.success("Таблица очищена.")
