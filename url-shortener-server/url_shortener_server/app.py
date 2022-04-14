import logging

from flask import Flask
from url_shortener_server import views

app = Flask(__name__)

app.logger.setLevel(logging.INFO)

app.add_url_rule("/api/long-urls/", view_func=views.URLLongView.as_view("long-urls"))
app.add_url_rule(
    "/api/short-urls/<string:short_url>/",
    view_func=views.URLShortView.as_view("short-urls"),
)
app.add_url_rule(
    "/<string:short_url>/", view_func=views.URLRedirectView.as_view("redirect-urls")
)
