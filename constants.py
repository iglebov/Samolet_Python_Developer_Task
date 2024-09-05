import pandas as pd

DAYS_LIST = (
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
)
DAYS_SERIES = pd.Series({DAYS_LIST[i]: i for i in range(7)})
TREES = ("Яблоня", "Слива", "Груша", "Вишня", "Черешня", "Персик")
STATES = (
    "insert_state",
    "change_state",
    "output_state",
    "plot_state",
    "random_state",
    "clear_state",
)
DEFAULT_SLEEP_TIME = 2

INSERT_BUTTON_CSS_STYLE = """
    button {
        display: block;
        margin: auto;
        height: 80px;
        width: 200px;
        background-color: #A4ff96;
        color: black;
    }"""

CHANGE_BUTTON_CSS_STYLE = """
    button {
        display: block;
        margin: auto;
        height: 80px;
        width: 200px;
        background-color: #FF96A4;
        color: black;
    }"""

OUTPUT_BUTTON_CSS_STYLE = """
    button {
        display: block;
        margin: auto;
        height: 80px;
        width: 200px;
        background-color: #96A4FF;
        color: black;
    }"""

PLOT_BUTTON_CSS_STYLE = """
    button {
        display: block;
        margin: auto;
        height: 80px;
        width: 200px;
        background-color: #F2C822;
        color: black;
    }"""

RANDOM_BUTTON_CSS_STYLE = """
    button {
        display: block;
        margin: auto;
        height: 80px;
        width: 200px;
        background-color: #DC82DA;
        color: black;
    }"""

CLEAR_BUTTON_CSS_STYLE = """
    button {
        display: block;
        margin: auto;
        height: 80px;
        width: 200px;
        background-color: #998BCF;
        color: black;
    }"""
