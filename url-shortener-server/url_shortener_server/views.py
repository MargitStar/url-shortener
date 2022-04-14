from re import S

from flask import jsonify, request
from flask.views import MethodView
from url_shortener_db.models import URL
from url_shortener_server.serializers import URLLongSchema, URLShortSchema
from url_shortener_server.settings import app


class URLLongView(MethodView):
    def post(self):
        urls = URLLongSchema().load(request.json)
        result = URL.add(**urls)
        return jsonify(URLShortSchema().dump(result)), 201


class URLShortView(MethodView):
    def get(self, short_url):
        result = URL.get_by_short_url(short_url=short_url)
        return jsonify(URLLongSchema().dump(result)), 200


app.add_url_rule("/api/long-urls/", view_func=URLLongView.as_view("long-urls"))

app.add_url_rule(
    "/api/short-urls/<string:short_url>/", view_func=URLShortView.as_view("short-urls")
)
