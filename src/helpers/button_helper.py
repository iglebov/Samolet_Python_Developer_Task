import streamlit

from src.constants import STATES


def hide_others_states(st: streamlit, unique_state: str) -> None:
    for state in STATES:
        if state != unique_state:
            setattr(st.session_state, state, False)
