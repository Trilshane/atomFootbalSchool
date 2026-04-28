FROM node:20-alpine

WORKDIR /app

# Кешируем node_modules
COPY package*.json ./
RUN npm install

# Исходники монтируются через volumes
EXPOSE 3000