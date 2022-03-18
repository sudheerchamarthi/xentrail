FROM python:alpine3.7
COPY src  /app
WORKDIR /app/
RUN pip install -r requirements.txt
ENV PORT=80
ENV AWS_REGION="us-east-1"
ENV DYNAMO_TABLE_NAME="xentrail"
ENTRYPOINT [ "python", "/app/app.py" ]
