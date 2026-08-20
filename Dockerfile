FROM python:3.10

RUN apt update && apt install -y git
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip install -U pip && pip install -U -r requirements.txt       
WORKDIR /app

COPY . .

CMD ["python3", "bot.py"]
