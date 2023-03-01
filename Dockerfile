FROM python:3.10.6-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY wsgi.py wsgi.py
COPY blog ./blog
COPY .env .env
EXPOSE 5000
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]

