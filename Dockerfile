FROM python:3.13.2-slim

WORKDIR /app
COPY . .

CMD ["python", "app.py"]