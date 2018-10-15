#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Простой скрипт, автоматически обновляющий резюме на hh.ru
Для автоматического обновления - создайте задачу в `crontab`.
"""

import requests

from secrets import URL, HEADER, RESPONSE_STATUS


def main():
    """Функция c основной логикой."""
    req = requests.post(URL, headers=HEADER)

    err: str = "Ошибка! Неправильный код ответа."
    message = RESPONSE_STATUS.get(req.status_code, err)
    print(message)


if __name__ == "__main__":
    main()
