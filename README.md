## Автоматическое обновление резюме на hh

Простой скрипт, обновляющий ваше резюме на `hh.ru`

### Установка

Первым делом, вставьте свой `токен` и `id` своего резюме в *secrets.py* файл.

Получить __token__ можно здесь -> https://dev.hh.ru/admin.

Получить __id__ -> перейдите на страницу с вашим резюме и укажите его `id`.

Рекомендуется использовать свежую версию компилятора python3.7

Установите необходимый пакет:

```bash
# С помощью pipenv -> https://github.com/pypa/pipenv/
pipenv install
```

### Использование

```bash
pipenv run python src/update_resume.py
```

### Crontab

Обновить резюме можно раз в 4 часа:

```bash
echo "0 */4 * * * python /путь/до/main.py" | crontab
```
