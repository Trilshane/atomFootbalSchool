FROM node:20-alpine

WORKDIR /app

# Копируем только package-файлы для кеширования слоёв
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем исходный код
COPY . .

# Открываем порт и настраиваем окружение
EXPOSE 3000
ENV NODE_ENV=development
ENV HOSTNAME=0.0.0.0
ENV PORT=3000

# Запускаем dev-сервер
CMD ["npm", "run", "dev"]