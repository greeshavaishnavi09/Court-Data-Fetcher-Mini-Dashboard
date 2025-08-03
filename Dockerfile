# Use official Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose the port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
