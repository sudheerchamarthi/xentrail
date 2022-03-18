FROM python:alpine3.7
COPY src  /app
WORKDIR /app/
RUN pip install -r requirements.txt
ENV PORT=80
ENTRYPOINT [ "python", "/app/app.py" ]
