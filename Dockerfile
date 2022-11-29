FROM python:3.8-alpine

WORKDIR /flask-app
COPY ./requirements.txt /flask-app/requirements.txt
RUN pip install -r requirements.txt

COPY flask-app.py /flask-app
COPY ./app /flask-app/app

ENTRYPOINT [ "python" ]
CMD ["flask-app.py" ]