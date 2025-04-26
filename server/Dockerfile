# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Command to run the app (update as needed)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
