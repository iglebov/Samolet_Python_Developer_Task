import pandas as pd

DAYS_SERIES = pd.Series(
    {
        "Понедельник": 0,
        "Вторник": 1,
        "Среда": 2,
        "Четверг": 3,
        "Пятница": 4,
        "Суббота": 5,
        "Воскресенье": 6,
    }
)

DAYS_LIST = [
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
]
TREES = ("Яблоня", "Слива", "Груша", "Вишня", "Черешня", "Персик")

DAYS_FOR_RADIO_BUTTON = (
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
