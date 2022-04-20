import logging

from flask import Flask
from url_shortener_server.base_routers import initialize_routes

app = Flask(__name__)

app.logger.setLevel(logging.INFO)
initialize_routes(app)
