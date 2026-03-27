# Use official lightweight Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Command to run your app
# Using -u to see python logs in real-time in docker console
CMD ["python", "-u", "main.py"]