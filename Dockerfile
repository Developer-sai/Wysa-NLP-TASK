# Use a lightweight Python image
FROM python:3.8-slim

WORKDIR /app

COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# Start the Flask API
CMD ["python", "app.py"]
