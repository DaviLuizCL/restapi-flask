FROM python:3.10-alpine3.19

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt



COPY wsgi.py config.py application/ ./

CMD ["python", "wsgi.py"]