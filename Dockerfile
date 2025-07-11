FROM python:3.11.0-alpine

COPY . /app/

WORKDIR /app

RUN mkdir logs && pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]