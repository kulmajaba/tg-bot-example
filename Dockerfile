# Image setup
FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv

WORKDIR /src

# Install python dependencies
COPY Pipfile /src
COPY Pipfile.lock /src
RUN pipenv install --system --deploy

# Copy code
COPY ./* /src

# Entry point
CMD ["python", "bot.py"]