# образ на основе которого создаём контейнер
FROM python:3.8-slim-buster

# рабочая директория внутри проекта
WORKDIR /home/project/fast_api

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# init
RUN apt-get update
RUN apt-get install -y --no-install-recommends gcc libc-dev

# django
RUN apt-get install -y build-essential libsqlite3-dev libpng-dev libjpeg-dev

# postgresql
RUN apt-get -y install libpq-dev gcc

# other
RUN apt-get install -y build-essential g++ flex bison gperf ruby perl \
libfontconfig1-dev libicu-dev libfreetype6 libssl-dev \
libpng-dev libjpeg-dev python libx11-dev libxext-dev

# устанавливаем зависимости
RUN pip install --upgrade pip
# копируем содержимое текущей папки в контейнер
COPY . .
RUN pip --no-cache-dir install -r req.txt





