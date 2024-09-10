# Samolet_Python_Developer_Task
Тестовое задание на позицию Python-разработчик в компанию Самолет.
### TODO
- [x] Строки 45:47 - Неправильное использование функционала строки с тройными кавычками.
В таких строках можно делать переносы строк.
В данном случае можно было использовать просто двойные кавычки. Либо 1 раз конструкцию:
f"""
...
"""
- [ ] Функция update вставляет значения в виде строки, даже если передается число.
То есть количество фруктов и температура хранятся как строки. Что неверно.
- [x] FruitFrame и ButtonHelper:
Лишнее сохранение библиотеки streamlit как атрибута класса.
- [x] Излишне сложная установка значений в st.session_state:
setattr(self.st.session_state, state, False) | Можно просто так: st.session_state[state] = False
- [x] Добавить БД
- [x] Добавить парсер погоды
- [x] За один день можно добавить несколько значений по одному и тому же дереву (ограничить)
- [x] В режиме редактирования запретить ввод отрицательных значений
- [x] В режиме редактирования таблицы можно поменять название дня недели и все ломается
- [x] В режиме редактирования нет проверки на отрицательные значения
- [x] В режиме редактирования также можно удалить название дерева
- [x] Ошибки в логике и валидации: сайт позволяет внести отрицательные значения в поле количества фруктов, хоть и подсвечивает что нельзя, в итоге в таблицу идет значение 1;
- [x] Min кол-во плодов должно быть 0
- [x] Много дублирования кода в fruit_info.py и файле с константами
- [x] st.markdown устаревшая конструкция, больше не используется
- [x] При введении данных выводится текст «True»
- [x] В начале названий фильтров стоит Select (особенности библиотеки streamlit dynamic filters)
- [x] График лучше сделать линейным и пошире
