#!flask/bin/python
from flask import Flask
import subprocess
import logging
import time;    

logging.basicConfig(filename='/home/sovietspy2/log/api.log',level=logging.INFO)

app = Flask(__name__)

@app.route('/publish')
def index():
    current_time = time.asctime( time.localtime(time.time()) )
    subprocess.call("git pull")
    subprocess.call("npm build")
    logging.info('Pull @ '+current_time)
    return "OK"

if __name__ == '__main__':
    app.run(debug=False, port=8000)