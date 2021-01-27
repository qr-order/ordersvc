FROM python:3.9-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY ./ ./

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--reload"]
