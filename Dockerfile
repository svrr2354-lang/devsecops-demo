# Use a lightweight Python Linux image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency file first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app code
COPY . .

# Tell Docker we are listening on port 5000
EXPOSE 5000

# The command to run when the container starts
CMD ["python", "app.py"]