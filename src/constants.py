import pandas as pd

DAYS_TUPLE = (
    "Понедельник",
    "Вторник",
    "Среда",
    "Четверг",
    "Пятница",
    "Суббота",
    "Воскресенье",
)
COLUMNS = {
    "День недели": "day",
    "Название дерева": "tree_name",
    "Кол-во фруктов": "fruits_number",
    "Средняя температура": "temperature",
}
COLUMNS_LIST = [
    "День недели",
    "Название дерева",
    "Кол-во фруктов",
    "Средняя температура",
]
BUTTONS_NAMES = {
    "insert_state": "Ввести",
    "change_state": "Изменить",
    "output_state": "Вывести",
    "plot_state": "График",
    "random_state": "Случайные данные",
    "clear_state": "Очистить",
}
DAYS_SERIES = pd.Series({DAYS_TUPLE[i]: i for i in range(7)})
TREES = ("Яблоня", "Слива", "Груша", "Вишня", "Черешня", "Персик")
STATES = (
    "insert_state",
    "change_state",
    "output_state",
    "plot_state",
    "random_state",
    "clear_state",
)
HTML_COLORS = {
    "green": "A4ff96",
    "red": "FF96A4",
    "blue": "96A4FF",
    "orange": "F2C822",
    "pink": "DC82DA",
    "dark": "998BCF",
}
DEFAULT_SLEEP_TIME = 2
