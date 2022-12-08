from flask import Flask
from datetime import datetime
import os
import mysql.connector

app = Flask(__name__)

@app.route('/')
def myrecord(x):
    return(x)

def hello():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    
    vmessage = "Opening Database now: "+date_time 
    mydb = mysql.connector.connect(host="localhost",user="root",password="Olor202@",database="em_schema")

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM ptb_reports")
    results = cursor.fetchall()

    for row in results:
        vmessage = row[1]
		    
    return vmessage

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
