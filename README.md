# Прогресс-календарь для мотивации

Это приложение-календарь, позволяющее отслеживать прогресс в различных активностях, таких как походы в спортзал, чтение книг, обучение и другие цели. В календаре можно отметить каждый день, когда вы выполнили задачу, а ячейки будут окрашиваться в зелёный в зависимости от количества выполненных действий. Чем больше активностей за день, тем темнее становится ячейка. Это помогает визуализировать достижения и поддерживать мотивацию в течение года.

## Как установить

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/kerplunk1/my_calendar.git
    ```

2. Перейдите в директорию проекта:

    ```bash
    cd my_calendar
    ```

3. Запустите приложение с использованием Docker:

    ```bash
    docker compose up -d
    ```

    После этого приложение будет доступно по адресу `http://localhost:8000` по умолчанию откроется текущий год.

## Как использовать

1. Чтобы выбрать нужный год, откройте в браузере:

    ```
    http://localhost:8000/<year>/
    ```

    Замените `<year>` на желаемый год (например, 2025).

2. Чтобы отметить текущий день, перейдите по следующему URL:

    ```
    http://localhost:8000/create/
    ```

    По умолчанию будет установлено действие "SPORT".

3. Чтобы отметить день с другим действием (например, чтение книги), используйте URL:

    ```
    http://localhost:8000/create/<action>/
    ```

    Замените `<action>` на нужное действие, например, `READING`.

    Примеры:
    - `http://localhost:8000/create/READING/`
    - `http://localhost:8000/create/LEARNING/`

---

![image](https://github.com/user-attachments/assets/99ecf446-cfae-4ca5-b4bc-5e1841d4beb5)


