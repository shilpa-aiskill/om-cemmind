FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py /app/main.py
EXPOSE 8080
# Print the PORT then start Uvicorn on it (Cloud Run injects $PORT)
CMD ["sh","-c","python - <<'P'\nimport os;print('Starting OM CemMind on PORT=', os.getenv('PORT','8080'))\nP\n && uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]
