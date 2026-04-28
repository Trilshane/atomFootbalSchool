FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Копируем зависимости отдельно для кеширования слоя
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Код монтируется через volumes, поэтому COPY . . не нужен для dev-режима
EXPOSE 8000