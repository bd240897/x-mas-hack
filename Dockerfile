FROM python:3.9-slim

EXPOSE 8501

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# устанавливаем зависимости
RUN pip install --upgrade pip
# копируем содержимое текущей папки в контейнер
COPY . .

RUN pip install -r requirements.txt

#ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]