FROM python:3.11-slim


WORKDIR /app


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


EXPOSE 5000

# Environment variables
ENV FLASK_ENV=production
ENV APP_VERSION=1.0.0


CMD ["python", "app.py"]
