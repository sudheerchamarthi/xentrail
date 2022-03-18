from flask import Flask
import platform
import datetime
import os
from datetime import date
app = Flask(__name__)
  
@app.route('/')
def myapp():
    START_DATE = os.environ.get('START_DATE')
    CANDIDATE_NBAME = os.environ.get('CANDIDATE_NBAME')
    return "Xendit - Trial - " + CANDIDATE_NBAME + " - "+ START_DATE + " - " + date.today().strftime("%Y/%m/%d")

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = os.environ.get('PORT'), debug = True) 
