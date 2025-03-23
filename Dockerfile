# Use slim Python image
FROM python:3.10-slim

# Install system dependencies
RUN apt update && apt install -y git cmake gcc nano libssl-dev python3-pip && \
    pip install cryptography

# Set runtime library path
ENV LD_LIBRARY_PATH=/usr/local/lib

# Build liboqs (shared libraries)
RUN git clone --branch main https://github.com/open-quantum-safe/liboqs.git /liboqs && \
    mkdir /liboqs/build && cd /liboqs/build && \
    cmake -DBUILD_SHARED_LIBS=ON .. && make -j2 && make install

# Build and install liboqs-python
RUN git clone --branch main https://github.com/open-quantum-safe/liboqs-python.git /liboqs-python && \
    cd /liboqs-python && \
    python3 -m pip install .

# Set working directory
WORKDIR /app

# Copy your hybrid CLI script
COPY cli_hybrid.py .

# Default command (can override)
CMD ["python3", "cli_hybrid.py"]
