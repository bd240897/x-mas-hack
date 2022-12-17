# Проект на хакатон X-MAS HACK 2022

Команда: **Сборная ХМН2 (1)**

## Оглавление
1. [Задача](#Задача)
2. [Архитектура](#Архитектура)
5. [Развёртывание решения](#Развёртывание-решения)
6. [Описание структуры папок проекта](#Описание-структуры-папок-проекта)
7. [Запуск](#Запуск)

## Задача
### Описание задачи
Придумать и реализовать прототип рекомендационной системы для подбора инвестиционных продуктов (сборка портфеля пользователя).

[:arrow_up:Оглавление](#Оглавление)

## Архитектура
    python 3.8
    backend/forntend - streamlit

[:arrow_up:Оглавление](#Оглавление)

## Развёртывание решения

Для удобства запуска приложения на разных платформах был использован `docker`. В папке `frontend` есть `dockerfile` который описывает состояние контейнера. Созданный контейнер будет оптравлен и развернут на удаленном сервере

### 1. Установка Docker (Ubuntu 20.04) 
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-ru

    sudo apt update
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
    sudo apt update
    apt-cache policy docker-ce
    sudo apt install docker-ce
    sudo systemctl status docker // status

### 2. Установка Docker-compose (Ubuntu 20.04)
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04-ru

    sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    docker-compose --version // status


### 3. Запуск через Docker-compose
https://webdevblog.ru/kak-ispolzovat-django-postgresql-i-docker/

    git clone https://github.com/bd240897/x-mas-hack
    cd x-mas-hack/
    docker-compose -f docker-compose.yml up --build -d
    
[:arrow_up:Оглавление](#Оглавление)

## Описание структуры папок проекта
  **api.py** - точка входа
- **pages** - страницы сайта
  - ...
- **logic** - вынесенная логика
  - ...

[:arrow_up:Оглавление](#Оглавление)

## Запуск
Протестировать уже запущенный сайт можно по ссылке:</br>

    http://51.250.65.65:8501/ (доступен на момент предоставления решения)
    # или
    http://localhost:8501/ (доступен при создании локального проекта)

[:arrow_up:Оглавление](#Оглавление)

## Заметки
```
