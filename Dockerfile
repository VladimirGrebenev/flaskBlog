FROM python:3.10.6-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY wsgi.py wsgi.py
COPY blog ./blog
EXPOSE 5000
CMD ["python", "flask", "db", "upgrade"]
CMD ["python", "flask", "create_admin"]
CMD ["python", "flask", "create_tags"]
CMD ["python", "wsgi.py"]

