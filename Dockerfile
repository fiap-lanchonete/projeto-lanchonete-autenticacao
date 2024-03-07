FROM python:3.10.13-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app

EXPOSE 8000

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
