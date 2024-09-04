import pandas as pd
import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from constants import (
    CHANGE_BUTTON_CSS_STYLE,
    DAYS_FOR_RADIO_BUTTON,
    INPUT_BUTTON_CSS_STYLE,
    OUTPUT_BUTTON_CSS_STYLE,
    PLOT_BUTTON_CSS_STYLE,
)
from FruitFrame import FruitFrame

st.markdown(
    "<h1 style='text-align: center;'>Информация о плодах</h1>", unsafe_allow_html=True
)

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


def _hide_all_except_insert() -> None:
    """Скрывает содержимое под кнопками 'Изменить' и 'Вывести'."""
    st.session_state.output_state = False
    st.session_state.change_state = False
    st.session_state.plot_state = False


def _hide_all_except_change() -> None:
    """Скрывает содержимое под кнопками 'Вывести' и 'Вставить'."""
    st.session_state.output_state = False
    st.session_state.insert_state = False
    st.session_state.plot_state = False


def _hide_all_except_output() -> None:
    """Скрывает содержимое под кнопками 'Вставить' и 'Изменить'."""
    st.session_state.insert_state = False
    st.session_state.change_state = False
    st.session_state.plot_state = False


def _hide_all_except_plot() -> None:
    """Скрывает содержимое под кнопками 'Вставить' и 'Изменить'."""
    st.session_state.insert_state = False
    st.session_state.change_state = False
    st.session_state.output_state = False


with stylable_container(
    "green",
    css_styles=INPUT_BUTTON_CSS_STYLE,
):
    insert = st.button("Ввести", on_click=_hide_all_except_insert)

if insert or st.session_state.insert_state:
    st.session_state.insert_state = True
    with st.form(key="fruits_info"):
        day_name = st.radio(
            "День недели",
            *DAYS_FOR_RADIO_BUTTON,
        )
        tree_name = st.text_input(label="Название дерева (Например: 'Яблоня')")
        fruits_number = st.number_input(
            label="Число плодов (Например: 1)", min_value=0, value=0
        )

        submit_form = st.form_submit_button(label="Добавить информацию")

        if submit_form:
            st.write(submit_form)

            if tree_name:
                row = pd.Series(
                    {
                        "День недели": day_name,
                        "Название дерева": tree_name,
                        "Кол-во фруктов": fruits_number,
                    }
                )
                st.session_state["fruit_frame"].insert(row)
                st.success("Информация успешно добавлена!")
            else:
                st.warning("Пожалуйста, заполните все поля.")

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
    st.bar_chart(
        st.session_state["fruit_frame"].data,
        x="День недели",
        y="Кол-во фруктов",
        x_label="День недели",
        y_label="Кол-во фруктов",
        color="Название дерева",
    )
