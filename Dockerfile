FROM python:3.8-alpine

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY zesty-secret-retriever.py /app
COPY ./app /app/app

ENTRYPOINT [ "python" ]
CMD ["zesty-secret-retriever.py" ]