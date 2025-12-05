FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Run Next dev binding to 0.0.0.0 so the dev server is reachable from the host
CMD ["npm", "run", "dev", "--", "-H", "0.0.0.0"]
