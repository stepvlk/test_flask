import gzip
import json
import sys

import toml
from flask import Flask, Response, jsonify, request

from routes import routes



app = Flask(__name__)
app.register_blueprint(routes)
config = toml.load('')
app.config['DEBUG'] = config['server']['loglevel']


if __name__ == "__main__":
    app.run() 