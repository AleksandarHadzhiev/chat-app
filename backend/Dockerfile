FROM python:3.12-slim

WORKDIR /

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv --version
RUN pipenv install 

COPY  . .

EXPOSE 8000

CMD ["pipenv", "run", "docker"]