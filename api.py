#!flask/bin/python
from flask import Flask
import subprocess
import logging
import time

logging.basicConfig(filename='/home/sovietspy2/log/api.log',level=logging.INFO)

app = Flask(__name__)

@app.route('/publish')
def index():
    current_time = time.asctime( time.localtime(time.time()) )
    subprocess.call("git -C /home/sovietspy2/www/phaser3Game/ pull",shell=True)
    logging.info('Pulled . . .')
    subprocess.call("npm install --prefix /home/sovietspy2/www/phaser3Game/",shell=True)
    logging.info('NPM install . . .')
    subprocess.call("npm run build --prefix /home/sovietspy2/www/phaser3Game/",shell=True)
    logging.info('NPM build . . . ')
    logging.info('finished @ '+current_time)
    return "OK"

if __name__ == '__main__':
    app.run(debug=True, port=8000)