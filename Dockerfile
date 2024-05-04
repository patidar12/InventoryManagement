FROM python:3.9

RUN mkdir -p /catalog

COPY . /catalog

WORKDIR /catalog

COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python", "run.py"]

