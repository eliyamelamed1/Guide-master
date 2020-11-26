# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /code/


# • PYTHONUNBUFFERED ensures our console output looks familiar and is not buffered by Docker, which we don’t want
# • PYTHONDONTWRITEBYTEcode means Python will not try to write .pyc files which we also do not desire

# A Docker image is a snapshot in time of what a project contains. It is represented by a Dockerfile
# and is literally a list of instructions that must be built - the image is the blueprint or set of
# plans for the apartment
