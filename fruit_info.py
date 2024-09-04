import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from constants import (
    CHANGE_BUTTON_CSS_STYLE,
    CLEAR_BUTTON_CSS_STYLE,
    INSERT_BUTTON_CSS_STYLE,
    OUTPUT_BUTTON_CSS_STYLE,
    PLOT_BUTTON_CSS_STYLE,
    RANDOM_BUTTON_CSS_STYLE,
)
from FruitFrame import FruitFrame

st.markdown(
    "<h1 style='text-align: center;'>Информация о плодах</h1>", unsafe_allow_html=True
)

st.markdown("###")

if "fruit_frame" not in st.session_state:
    st.session_state["fruit_frame"] = FruitFrame()
if "insert_state" not in st.session_state:
    st.session_state.insert_state = False
if "change_state" not in st.session_state:
    st.session_state.change_state = False
if "output_state" not in st.session_state:
    st.session_state.output_state = False
if "plot_state" not in st.session_state:
    st.session_state.plot_state = False
if "random_state" not in st.session_state:
    st.session_state.random_state = False
if "clear_state" not in st.session_state:
    st.session_state.clear_state = False


def _hide_all_except_insert() -> None:
    """Скрывает содержимое всех кнопок, кроме 'Ввести'."""
    st.session_state.output_state = False
    st.session_state.change_state = False
    st.session_state.plot_state = False
    st.session_state.clear_state = False
    st.session_state.random_state = False


def _hide_all_except_change() -> None:
    """Скрывает содержимое всех кнопок, кроме 'Изменить'."""
    st.session_state.output_state = False
    st.session_state.insert_state = False
    st.session_state.plot_state = False
    st.session_state.clear_state = False
    st.session_state.random_state = False


def _hide_all_except_output() -> None:
    """Скрывает содержимое всех кнопок, кроме 'Вывести'."""
    st.session_state.insert_state = False
    st.session_state.change_state = False
    st.session_state.plot_state = False
    st.session_state.clear_state = False
    st.session_state.random_state = False


def _hide_all_except_plot() -> None:
    """Скрывает содержимое всех кнопок, кроме 'График'."""
    st.session_state.insert_state = False
    st.session_state.change_state = False
    st.session_state.output_state = False
    st.session_state.clear_state = False
    st.session_state.random_state = False


def _hide_all_except_random() -> None:
    """Скрывает содержимое всех кнопок, кроме 'Случайные данные'."""
    st.session_state.insert_state = False
    st.session_state.change_state = False
    st.session_state.output_state = False
    st.session_state.plot_state = False
    st.session_state.clear_state = False


def _hide_all_except_clear() -> None:
    """Скрывает содержимое всех кнопок, кроме 'Очистить'."""
    st.session_state.insert_state = False
    st.session_state.change_state = False
    st.session_state.output_state = False
    st.session_state.plot_state = False
    st.session_state.random_state = False


with stylable_container(
    "green",
    css_styles=INSERT_BUTTON_CSS_STYLE,
):
    insert = st.button("Ввести", on_click=_hide_all_except_insert)

if insert or st.session_state.insert_state:
    st.session_state.insert_state = True
    st.session_state["fruit_frame"].form(st)

with stylable_container(
    "red",
    css_styles=CHANGE_BUTTON_CSS_STYLE,
):
    change = st.button("Изменить", on_click=_hide_all_except_change)

if change or st.session_state.change_state:
    st.session_state.change_state = True
    st.session_state["fruit_frame"].change(st)

with stylable_container(
    "blue",
    css_styles=OUTPUT_BUTTON_CSS_STYLE,
):
    output = st.button("Вывести", on_click=_hide_all_except_output)

if output or st.session_state.output_state:
    st.session_state.output_state = True
    st.session_state["fruit_frame"].output()

with stylable_container(
    "orange",
    css_styles=PLOT_BUTTON_CSS_STYLE,
):
    plot = st.button("График", on_click=_hide_all_except_plot)

if plot or st.session_state.plot_state:
    st.session_state.plot_state = True
    st.session_state["fruit_frame"].plot(st)

with stylable_container(
    "pink",
    css_styles=RANDOM_BUTTON_CSS_STYLE,
):
    random = st.button("Случайные данные", on_click=_hide_all_except_random)

if random or st.session_state.random_state:
    st.session_state.random_state = True
    st.session_state["fruit_frame"].random()
    st.success("Добавлено 10 случайных строк!")

with stylable_container(
    "dark",
    css_styles=CLEAR_BUTTON_CSS_STYLE,
):
    clear = st.button("Очистить", on_click=_hide_all_except_clear)

if clear or st.session_state.clear_state:
    st.session_state.clear_state = True
    st.session_state["fruit_frame"].clear()
    st.success("Таблица очищена")
