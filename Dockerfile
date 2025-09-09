# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install OS-level dependencies
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    wget \
    libxml2 \
    libxslt1.1 \
    zlib1g \
    libjpeg62-turbo \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose port if needed (optional, for webhooks)
EXPOSE 5000

# Command to run the bot
CMD ["python3", "bot.py"]
