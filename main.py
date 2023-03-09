# -*- coding: UTF-8 -*-
import sys
from flask import Flask
from flask_cors import CORS
from gevent import pywsgi, monkey

monkey.patch_all()

app = Flask(
    __name__,
    static_folder='web',
    static_url_path=''
)

def after_request(resp):
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

app.after_request(after_request)
app.config['JSON_AS_ASCII'] = False
CORS(app, supports_credentials=True)

@app.route('/', methods=['GET'])
def home():
    return "<p>Hello World!</p>"


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 1024
    print('@启动服务...')
    print("@本地调试：http://{}:{}".format(host, port))
    if len(sys.argv) > 1 and sys.argv[1] == 'debug':
        app.run(host=host, port=port)
    else:
        server = pywsgi.WSGIServer((host, port), app)
        server.serve_forever()