
FROM python:3.10

RUN apt-get update --fix-missing


RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-jpn \
    vim \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/* 

RUN apt-get install -y tesseract-ocr-jpn


RUN pip install --no-cache-dir pytesseract pillow numpy opencv-python fuzzywuzzy python-Levenshtein


WORKDIR /app


COPY . /app

