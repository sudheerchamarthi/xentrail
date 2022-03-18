from flask import Flask
import boto3
import datetime
import os
from datetime import date
app = Flask(__name__)
  
@app.route('/')
def myapp():
    REGION = os.environ.get('AWS_REGION')
    DYNAMO_TABLE_NAME = os.environ.get('DYNAMO_TABLE_NAME')
    client = boto3.client('dynamodb',region_name=REGION)
    client.put_item(TableName=DYNAMO_TABLE_NAME, Item={"timestamp":{'S':str(round(datetime.datetime.utcnow().timestamp() * 1000))},'logging':{'S':"Yes"} })
    return "Success!. Logged entry in DB with Timestamp"

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = os.environ.get('PORT'), debug = True) 
