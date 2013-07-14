from flask import Flask, url_for
from flask import request
from flask import render_template
import json
import time

app = Flask(__name__)


LAST_FETCH_TIMESTAMP = time.time()
EXPIRE_TIME = 10 * 60

def isExpire():
    print "----------------------------->"
    cur_time = time.time();
    # time_span = cur_time - LAST_FETCH_TIMESTAMP;
    print cur_time
    print type(cur_time)
    print LAST_FETCH_TIMESTAMP    

    LAST_FETCH_TIMESTAMP = cur_time;
    # if time_span > EXPIRE_TIME:
    #     return True
    # else:
    #     return False
    return LAST_FETCH_TIMESTAMP

@app.route('/')
def comein():
    isExpire()
    return render_template('index.html')


@app.route('/login')
def login():
    print isExpire()
    return json.dumps({
        'time': timeStamp,
        'status': 'ok'
    })


@app.errorhandler(404)
def page_not_found(error):
    return "wrong"


app.config.update(
    DEBUG = True,
    SERVER_NAME = "127.0.0.1:8000"
)

if __name__ == '__main__':
    app.run()