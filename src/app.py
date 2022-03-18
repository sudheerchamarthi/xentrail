from flask import Flask
import platform
import datetime
import os
from datetime import date
app = Flask(__name__)
  
@app.route('/')
def myapp():
    #Reurn OS
    return "My OS is " +  str(platform.platform())
    
if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = os.environ.get('PORT'), debug = True) 
