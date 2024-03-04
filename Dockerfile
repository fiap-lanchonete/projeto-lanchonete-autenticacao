FROM python:3.10.13-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

EXPOSE 8000

CMD [" gunicorn", "--bind", "0.0.0.0:8000", "app:create_app()" ]
