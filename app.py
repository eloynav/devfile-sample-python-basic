from flask import Flask
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    vmessage = "Hello World! Today is: "+date_time 


    return vmessage

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')