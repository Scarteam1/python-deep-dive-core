# Stage 1: Build & Dependency isolation
FROM python:3.10-slim AS builder
WORKDIR /app
RUN pip install --no-cache-dir numpy

# Stage 2: Minimalist Production Run Image (Secure and small)
FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY . /app

EXPOSE 8000
CMD ["python", "profile_memory.py"]
