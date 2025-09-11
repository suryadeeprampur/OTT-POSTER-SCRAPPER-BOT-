# ------------------- Base Image ------------------- #
FROM python:3.11-slim

# ------------------- Working Directory ------------------- #
WORKDIR /app

# ------------------- Environment Variables ------------------- #
ENV TZ=UTC

# ------------------- Install OS-level dependencies ------------------- #
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
        ntpdate \
    && ln -fs /usr/share/zoneinfo/$TZ /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*

# ------------------- Copy Project Files ------------------- #
COPY . /app

# ------------------- Upgrade pip & Install Python dependencies ------------------- #
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ------------------- Expose Port (optional) ------------------- #
EXPOSE 5000

# ------------------- Command to Sync Time and Run Bot ------------------- #
CMD ntpdate -u pool.ntp.org && python bot.py
