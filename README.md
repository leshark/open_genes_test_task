# Тестовое задание на python backend разработчика

## Описание задачи

Имеются данные по экспериментам на двух модельных организмах: мышах и червях.

Данные сохранены в двух csv-файлах [test_data](https://drive.google.com/drive/folders/16PVqwOGgErci0LPDZOMrHz9z1nAisaGW) с полями:
* `Compound/Formulation` - действующее вещество в эксперименте
* `Species` - вид модельного организма
* `Avg/Med Lifespan Change (%)` - изменение продолжительности жизни в результате эксперимента
* `Reference` - ссылка на исследование

Нужно реализовать:
* разработать структуру БД для хранения данных по этим экспериментам в 3НФ.
* написать миграцию для поднятия базы с нужной структурой
* написать консольный скрипт, запускающий миграцию и заполняющий базу данными из csv. Вещества и модельные организмы должны быть уникальными.
* написать запрос к БД, который вернет список веществ и максимальные значения изменения продолжительности жизни по ним для обоих видов в формате:


| compound | species | max_med_lifespan_change |
| ----------- | ----------- | ----------- |
| Caffeine | Caenorhabditis elegans | 7.7 |
| Rapamycin | Mus musculus | 13 |
| Rapamycin | Caenorhabditis elegans | 26 |
| Nordihydroguaiaretic acid | Mus musculus | 12 |


Требования к реализации:
* код миграций и скрипта на заполнение на python 3.*
* БД mysql / mariadb
* запрос к БД - на голом SQL
* запушить все в публичный репозиторий

По желанию можно еще:
* завернуть в docker-compose
* сформировать в pandas из приведенных датасетов такой же ответ, как из запроса в задании

## Реализация

* Бекенд фреймворк - `FastAPI`
* Миграции - при помощи `alembic`
* Скрипт заполнения базы данными - `fill_db.py`
* Управление зависимостями - `poetry`

## Структура бд

![](https://i.ibb.co/zfqHGZH/db-diagram.png)

## Деплой
Деплой выполняется при помощи docker-compose

1. `docker-compose build`
2. `docker-compose up -d`

> При первом запуске необходимо подсоединиться к контейнеру `web` и заполнить базу:
```
python fill_db.py
```
сваггер доступен по: `http://127.0.0.1:8000/api/docs`
