FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

COPY . /app/


RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["gunicorn", "setup.wsgi:application", "--bind", "0.0.0.0:8000"]

