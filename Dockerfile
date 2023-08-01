# Stage 1: Build React frontend
FROM node:14-alpine AS frontend-build

WORKDIR /app/frontend
COPY frontend/package*.json ./
RUN npm install
COPY frontend/ .
RUN npm run build

# Stage 2: Build Python Flask backend
FROM python:3.8-slim-buster AS backend-build

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/backend
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Stage 3: Production
FROM python:3.8-slim-buster AS production

COPY --from=backend-build /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=backend-build /usr/local/bin/gunicorn /usr/local/bin/

WORKDIR /app
COPY --from=frontend-build /app/frontend/build /app/frontend/build
COPY backend/ .

# Expose port 5000 for the app
EXPOSE 5000

# Run the gunicorn server
CMD gunicorn --bind 0.0.0.0:${PORT} app:app
