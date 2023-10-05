FROM tiangolo/uvicorn-gunicorn:python3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV DOCKER_BUILDKIT 1

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app

COPY . .

VOLUME /app

CMD ["uvicorn", "app.api.server:app", "--reload", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]

