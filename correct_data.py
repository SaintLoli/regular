import re

def is_valid_date(date_str):
    # Основные компоненты
    day = r'(0?[1-9]|[12][0-9]|3[01])'
    month_num = r'(0?[1-9]|1[0-2])'
    year = r'\d+'
    month_rus = r'(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)'
    month_eng = r'(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)'

    separators = [
        (r'\.', r'\.'),  # точка
        (r'/', r'/'),  # слэш
        (r'-', r'-')  # дефис
    ]

    num_patterns = [rf'^{day}{i}{month_num}{j}{year}$' for i, j in separators]
    num_patterns += [rf'^{year}{i}{month_num}{j}{day}$' for i, j in separators]


    # Все шаблоны
    patterns = num_patterns + [
        # Текстовые форматы
        rf'^{day}\s+{month_rus}\s+{year}$',
        rf'^{month_eng}\s+{day},\s+{year}$',
        rf'^{year},\s+{month_eng}\s+{day}$'
    ]

    return any(re.fullmatch(p, date_str) for p in patterns)


print(is_valid_date(input("Введите дату для теста --> ")))