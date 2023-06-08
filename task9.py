from datetime import datetime
import re


def main(input_table):
    new_table = []
    seen = set()
    for row in input_table:
        row = list(filter(lambda item: item is not None, row))
        if len(row) != 0:
            row_tuple = tuple(row)
            if row_tuple not in seen:
                new_table.append(row)
                seen.add(row_tuple)
    for row in new_table:
        if row[0]:
            date_obj = datetime.strptime(row[0], "%Y/%m/%d")
            row[0] = date_obj.strftime("%d-%m-%y")
        if row[1]:
            row[1] = re.search(r"\b\w+$", row[1]).group(0)
        if row[2]:
            row[2] = re.sub(r"\D", "", row[2])[1:]
        if row[3]:
            row[3] = re.search(r"\[at](.+)$", row[3]).group(1)
    return new_table


print(
    main(
        [
            [
                "2004/04/13",
                None,
                "Вячеслав Г. Цебакянц",
                None,
                "+7 (691) 892-54-64",
                "vaceslav63[at]yahoo.com",
            ],
            [
                "2003/02/17",
                None,
                "Руслан И. Фушачак",
                None,
                "+7 (051) 566-56-18",
                "fusacak98[at]gmail.com",
            ],
            [
                "2004/05/16",
                None,
                "Макар Ш. Бумивянц",
                None,
                "+7 (734) 291-76-87",
                "bumivanz16[at]mail.ru",
            ],
            [
                "2004/05/16",
                None,
                "Макар Ш. Бумивянц",
                None,
                "+7 (734) 291-76-87",
                "bumivanz16[at]mail.ru",
            ],
            [],
            [],
            [
                "2004/05/16",
                None,
                "Макар Ш. Бумивянц",
                None,
                "+7 (734) 291-76-87",
                "bumivanz16[at]mail.ru",
            ],
            [
                "1999/03/18",
                None,
                "Валерий Г. Кидук",
                None,
                "+7 (481) 922-22-43",
                "valerij85[at]mail.ru",
            ],
        ]
    )
)
