from datetime import datetime


def is_valid_date(date_str):
    months_ru = {
        'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4,
        'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
        'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12
    }

    date_formats = [
        '%d.%m.%Y', '%d/%m/%Y', '%d-%m-%Y',
        '%Y.%m.%d', '%Y/%m/%d', '%Y-%m-%d',
        '%B %d, %Y', '%b %d, %Y',
        '%Y, %B %d', '%Y, %b %d',
    ]

    for fmt in date_formats:
        try:
            date_obj = datetime.strptime(date_str, fmt)
            if date_obj.year >= 0:
                return True
        except ValueError:
            continue

    parts = date_str.split()
    if len(parts) == 3:
        try:
            day = int(parts[0])
            month_ru = parts[1]
            year = int(parts[2])

            if month_ru in months_ru and year >= 0:
                month = months_ru[month_ru]
                datetime(year=year, month=month, day=day)
                return True
        except (ValueError, KeyError):
            pass

    return False


print(is_valid_date(input("Введите дату --> ")), sep="\n")