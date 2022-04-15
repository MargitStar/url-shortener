import logging

from flask import Flask
from flask_cors import CORS
from url_shortener_server.base_routers import initialize_routes

app = Flask(__name__)
CORS(app)

app.logger.setLevel(logging.INFO)
initialize_routes(app)
