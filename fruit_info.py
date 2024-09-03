import pandas as pd
import streamlit as st
from streamlit_extras.stylable_container import stylable_container

from data import df_with_filters, display_table, fruit_data, update_fruit_data

st.markdown(
    "<h1 style='text-align: center;'>Информация о плодах</h1>", unsafe_allow_html=True
)

with stylable_container(
    "green",
    css_styles="""
    button {
        background-color: #A4ff96;
        color: black;
    }""",
):
    insert = st.button("Ввести")

if "insert_state" not in st.session_state:
    st.session_state.insert_state = False

if insert or st.session_state.insert_state:
    st.session_state.insert_state = True
    st.session_state.output_state = False
    st.session_state.change_state = False

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
                update_fruit_data(
                    pd.concat([fruit_data, pd.DataFrame([row], columns=row.index)])
                )
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
    change = st.button("Изменить")

if "change_state" not in st.session_state:
    st.session_state.change_state = False

if change or st.session_state.change_state:
    st.session_state.change_state = True
    st.session_state.insert_state = False
    st.session_state.output_state = False

    st.data_editor(fruit_data)

with stylable_container(
    "blue",
    css_styles="""
    button {
        background-color: #96A4FF;
        color: black;
    }""",
):
    output = st.button("Вывести", on_click=display_table)

if "output_state" not in st.session_state:
    st.session_state.output_state = False

if output or st.session_state.output_state:
    st.session_state.output_state = True
    st.session_state.change_state = False
    st.session_state.insert_state = False

    df_with_filters.display_filters()
    df_with_filters.display_df()

# TODO: Добавить график (pandas y - количество фруктов, x - день)
