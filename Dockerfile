# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only necessary file
COPY app.py .

# Install Flask
RUN pip install Flask

# Expose port for the container
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
