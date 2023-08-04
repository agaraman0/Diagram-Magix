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

# Add build-time environment variables
ARG OPENAI_API_KEY
ARG DIAGRAM_API
ARG EXTERNAL_DIAGRAM_API

# Translate build arguments to environment variables
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV DIAGRAM_API=${DIAGRAM_API}
ENV EXTERNAL_DIAGRAM_API=${EXTERNAL_DIAGRAM_API}

COPY --from=backend-build /usr/local/lib/python3.8/site-packages/ /usr/local/lib/python3.8/site-packages/
COPY --from=backend-build /usr/local/bin/gunicorn /usr/local/bin/

WORKDIR /app
COPY --from=frontend-build /app/frontend/build /app/frontend/build
COPY backend/ .

# Expose port 5000 for the app
EXPOSE 5000

# Run the gunicorn server
CMD gunicorn --workers 5 --timeout 150 --bind 0.0.0.0:${PORT} app:app
