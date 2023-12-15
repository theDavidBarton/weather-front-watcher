FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
