# Pull base image
FROM python:3.9.1

ARG WORKPATH=/usr/src/www/
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
# Set work directory
WORKDIR $WORKPATH

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirement.txt $WORKPATH
RUN pip install -r requirement.txt

# Copy project
COPY . $WORKPATH
