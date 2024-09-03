import pandas as pd
import streamlit as st
from streamlit_extras.stylable_container import stylable_container

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


def _hide_all_except_insert() -> None:
    """Скрывает содержимое под кнопками 'Изменить' и 'Вывести'."""
    st.session_state.output_state = False
    st.session_state.change_state = False


def _hide_all_except_change() -> None:
    """Скрывает содержимое под кнопками 'Вывести' и 'Вставить'."""
    st.session_state.output_state = False
    st.session_state.insert_state = False


def _hide_all_except_output() -> None:
    """Скрывает содержимое под кнопками 'Вставить' и 'Изменить'."""
    st.session_state.insert_state = False
    st.session_state.change_state = False


with stylable_container(
    "green",
    css_styles="""
    button {
        background-color: #A4ff96;
        color: black;
    }""",
):
    insert = st.button("Ввести", on_click=_hide_all_except_insert)

if insert or st.session_state.insert_state:
    st.session_state.insert_state = True
    with st.form(key="fruits_info"):
        day_name = st.radio(
            "День недели",
            (
                "Понедельник",
                "Вторник",
                "Среда",
                "Четверг",
                "Пятница",
                "Суббота",
                "Воскресенье",
            ),
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
    css_styles="""
    button {
        background-color: #FF96A4;
        color: black;
    }""",
):
    change = st.button("Изменить", on_click=_hide_all_except_change)

if change or st.session_state.change_state:
    st.session_state.change_state = True
    st.session_state["fruit_frame"].change(st)

with stylable_container(
    "blue",
    css_styles="""
    button {
        background-color: #96A4FF;
        color: black;
    }""",
):
    output = st.button("Вывести", on_click=_hide_all_except_output)

if output or st.session_state.output_state:
    st.session_state.output_state = True
    st.session_state["fruit_frame"].output()

# TODO: Добавить график (pandas y - количество фруктов, x - день)
