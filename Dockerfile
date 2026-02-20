# use the python 3.13-slim base image
FROM python:3.13-slim

LABEL authors="systemspro.tech"

# Update and install some useful tools
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# create and set a working directory to dump our files into
WORKDIR /app

# copy only the requirements.txt file
COPY ./EmailAnarchy/requirements.txt .

# copy our src directory to /app/src within container
COPY ./EmailAnarchy/src ./src

# pip install list of required python packages
RUN pip install --no-cache-dir -r requirements.txt

# open port 8501
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/app/_stcore/health

# run streamlit app
ENTRYPOINT ["streamlit", "run", "src/server.py", "--server.port=8501", "--server.address=0.0.0.0"]
