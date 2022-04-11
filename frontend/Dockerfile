FROM node:12 as builder
# Create and change to the app directory.
WORKDIR /app
COPY package*.json ./
RUN npm install
# Copy local code to the container image.
COPY . ./
RUN npm run build

FROM nginx
COPY --from=builder /app/build /usr/share/nginx/html