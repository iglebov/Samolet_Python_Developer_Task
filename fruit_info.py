import streamlit as st

from src.constants import STATES
from src.datatypes.fruit_frame import FruitFrame
from src.helpers.button_helper import ButtonHelper

_, col, _ = st.columns([1, 4, 1])
with col:
    st.title("Информация о плодах")

if "fruit_frame" not in st.session_state:
    st.session_state["fruit_frame"] = FruitFrame()
    st.session_state["button_helper"] = ButtonHelper()

for state in STATES:
    if state not in st.session_state:
        st.session_state[state] = False

insert = st.session_state["button_helper"].create_button(st, "green", "insert_state")
if insert or st.session_state.insert_state:
    st.session_state.insert_state = True
    st.session_state["fruit_frame"].form(st)

change = st.session_state["button_helper"].create_button(st, "red", "change_state")
if change or st.session_state.change_state:
    st.session_state.change_state = True
    st.session_state["fruit_frame"].change(st)

output = st.session_state["button_helper"].create_button(st, "blue", "output_state")
if output or st.session_state.output_state:
    st.session_state.output_state = True
    st.session_state["fruit_frame"].output()

plot = st.session_state["button_helper"].create_button(st, "orange", "plot_state")
if plot or st.session_state.plot_state:
    st.session_state.plot_state = True
    st.session_state["fruit_frame"].plot(st)

random = st.session_state["button_helper"].create_button(st, "pink", "random_state")
if random or st.session_state.random_state:
    st.session_state.random_state = True
    st.session_state["fruit_frame"].random()
    st.success("Добавлено 10 случайных строк!")

clear = st.session_state["button_helper"].create_button(st, "dark", "clear_state")
if clear or st.session_state.clear_state:
    st.session_state.clear_state = True
    st.session_state["fruit_frame"].clear()
    st.success("Таблица очищена.")
