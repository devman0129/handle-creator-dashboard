# this is the docker file for django behind gunicorn

FROM python:3.11-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



# install django dependencies
COPY ./requirements.txt ./

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # install postgres client so we can run pg commands if needed
    apk add --update --no-cache postgresql-client && \
    # install psycopg2 build dependencies into temporary build dependencies folder
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base gcc libc-dev linux-headers postgresql-dev musl-dev && \
    # install django requirements
    /py/bin/pip install -r requirements.txt && \
    # delete temporary build dependencies folder
    apk del .tmp-build-deps && \
    adduser --disabled-password --no-create-home appuser

RUN mkdir -p /mnt/web/static && \
    mkdir -p /mnt/web/media && \
    chown -R appuser:appuser /mnt/web && \
    chmod -R 755 /mnt/web



# add python venv to path so we can run python without activating the venv
ENV PATH="/py/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
RUN chmod +x /app/entrypoint.sh

# can switch to non-root user if needed

# USER appuser
# RUN adduser -D user
# USER user
# RUN chown -R user:user /app
# RUN chmod -R 755 /app


CMD ["/app/entrypoint.sh"]