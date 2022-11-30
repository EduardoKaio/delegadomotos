# pull official base image
FROM python:3.10.5

# set work directory
WORKDIR /usr/src/delegadomotos

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add mysqlclient gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/delegadomotos/entrypoint.sh
RUN chmod +x /usr/src/delegadomotos/entrypoint.sh

# copy project
COPY . .

ENTRYPOINT ["/usr/src/delegadomotos/entrypoint.sh"]