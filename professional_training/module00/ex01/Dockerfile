FROM node:14-alpine
WORKDIR /app
COPY index.html .
COPY server.js .
RUN npm init -y && npm install express@4.21.2
EXPOSE 8080
CMD ["node", "server.js"]
