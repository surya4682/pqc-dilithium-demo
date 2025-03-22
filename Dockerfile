FROM python:3.10-slim

# Install dependencies
RUN apt update && apt install -y git cmake gcc nano libssl-dev

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

# Set workdir
WORKDIR /app

# Copy your demo script
COPY cli_dilithium.py .

# Run the script
CMD ["python3", "cli_dilithium.py"]

