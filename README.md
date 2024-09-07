# Samolet_Python_Developer_Task
Тестовое задание на позицию Python-разработчик в компанию Самолет.
### TODO
- [ ] Добавить БД
- [ ] Добавить парсер погоды
- [ ] В режиме редактирования запретить ввод отрицательных значений
- [ ] В режиме редактирования таблицы можно поменять название дня недели и все ломается
- [ ] В режиме редактирования нет проверки на отрицательные значения
- [ ] В режиме редактироваиня также можно удалить название дерева
- [ ] За один день можно добавить несколько значений по одному и тому же дереву (ограничить)
- [x] Ошибки в логике и валидации: сайт позволяет внести отрицательные значения в поле количества фруктов, хоть и подсвечивает что нельзя, в итоге в таблицу идет значение 1;
- [x] Min кол-во плодов должно быть 0
- [x] Много дублирования кода в fruit_info.py и файле с константами
- [x] st.markdown устаревшая конструкция, больше не используется
- [x] При введении данных выводится текст «True»
- [x] В начале названий фильтров стоит Select (особенности библиотеки streamlit dynamic filters)
- [x] График лучше сделать линейным и пошире (https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart)
- [ ] Добавить тесты (для БД + для FruitFrame)
