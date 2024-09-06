import streamlit
from streamlit_extras.stylable_container import stylable_container

from src.constants import BUTTONS_NAMES, HTML_COLORS, STATES


class ButtonHelper:
    def __init__(self, st: streamlit):
        self.st = st

    def _hide_others_states(self, unique_state: str) -> None:
        for state in STATES:
            if state != unique_state:
                setattr(self.st.session_state, state, False)

    def create_button(self, color: str, state_name: str):
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
            return self.st.button(
                BUTTONS_NAMES[state_name],
                on_click=lambda: self._hide_others_states(state_name),
            )
