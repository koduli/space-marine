FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV DISPLAY=host.docker.internal:0

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-pygame \
    libsdl2-2.0-0 \
    libsdl2-image-2.0-0 \
    libsdl2-mixer-2.0-0 \
    libsdl2-ttf-2.0-0 \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the game files
COPY src/ /app/src/

# Create a simple startup script
RUN echo '#!/bin/bash\n\
python src/run.py' > /app/start.sh && chmod +x /app/start.sh

# Set the startup script as the entry point
ENTRYPOINT ["/app/start.sh"] 