FROM python:alpine3.7
COPY src  /app
WORKDIR /app/
RUN pip install -r requirements.txt
ENV PORT=8080
ENV START_DATE="2022-03-17"
ENV CANDIDATE_NBAME="Sudheer Chamarthi"
ENTRYPOINT [ "python", "/app/app.py" ]
