import streamlit
from streamlit_extras.stylable_container import stylable_container

from src.constants import BUTTONS_NAMES, HTML_COLORS, STATES


class ButtonHelper:
    @staticmethod
    def _hide_others_states(st: streamlit, unique_state: str) -> None:
        for state in STATES:
            if state != unique_state:
                st.session_state[state] = False

    @classmethod
    def create_button(cls, st: streamlit, color: str, state_name: str):
        with stylable_container(
            color,
            css_styles="""
            button {
                display: block;
                margin: auto;
                height: 80px;
                width: 200px;
                color: black;"""
            + f"background-color: #{HTML_COLORS[color]};"
            + "})",
        ):
            return st.button(
                BUTTONS_NAMES[state_name],
                on_click=lambda: cls._hide_others_states(st, state_name),
            )
