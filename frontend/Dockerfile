FROM node:18
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .
RUN chown -R 1000:1000 /app
USER 1000
CMD ["npm", "start"]
EXPOSE 3000
