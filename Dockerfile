# Use official Python slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Set timezone environment variable
ENV TZ=UTC

# Install OS-level dependencies + tzdata for time sync
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        ffmpeg \
        curl \
        wget \
        libxml2 \
        libxslt1.1 \
        zlib1g \
        libjpeg62-turbo \
        tzdata \
    && ln -fs /usr/share/zoneinfo/$TZ /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Upgrade pip and install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose port (optional, needed if bot has webhook)
EXPOSE 5000

# Command to run the bot
CMD ["python", "bot.py"]
