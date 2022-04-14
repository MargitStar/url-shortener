import logging

from flask import Flask

app = Flask(__name__)

app.logger.setLevel(logging.INFO)
