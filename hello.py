from flask import Flask, request
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)

@app.route('/')
def index():
    return "Your IP address is %s\n" % request.remote_addr

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)