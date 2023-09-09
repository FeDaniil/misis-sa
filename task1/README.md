# Задание 1

## Задание 1.1. Запись графа в файл формата CSV

Граф может быть представлен в виде матрицы смежности: `graph_matrix.csv`.

## Задание 1.2. Парсинг и извлечение данных из CSV и JSON

### CSV

Скрипт `csv_extract.py` извлекает данные из CSV-файла в заданном ряду и колонке.

Пример использования: `python3 csv_extract.py example.csv 1 2`. Помощь по использованию: `python3 csv_extract.py -h`.

### JSON

Скрипт `json_extract.py` извлекает данные из JSON-файла по заданному JSONPath (формат, напоминающий XPath, но изначально спроектированный для JSON).

Перед испоользованием, нужно установить зависимости: `pip3 install -r requirements.txt`.

Пример использования: `python3 json_extract.py example.json "$.str.str1[1]"`. Помощь по использованию: `python3 json_extract.py -h`.
