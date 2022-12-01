from flask import Flask
from datetime import datetime
from tkinter import *
import os

app = Flask(__name__)

@app.route('/')
def hello():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    vmessage = "Hello World! Today is: "+date_time 

    root = Tk()
    var = IntVar()
    R1 = Radiobutton(root, text = "HOG Application Summary", variable=var, value=1, command=sel)
    R1.pack(anchor = W)
    R2 = Radiobutton(root, text = "HOG Provincial Summary",  variable=var, value=2, command=sel)
    R2.pack(anchor = W)
    label = Label(root)
    label.pack()
    root.mainloop()

    return vmessage

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')