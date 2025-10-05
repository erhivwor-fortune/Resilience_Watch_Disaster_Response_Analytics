FROM python:3.13.6

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

#Can also use /app as the 2nd working directory.
COPY . . 

CMD ["python", "main.py"]
