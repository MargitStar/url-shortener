from flask import jsonify, redirect, request
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
        long_url = URL.get_by_short_url(short_url=short_url)
        return jsonify(URLLongSchema().dump(long_url)), 200


class URLRedirectView(MethodView):
    def get(self, short_url):
        long_url = URL.get_by_short_url(short_url=short_url)
        return redirect(URLLongSchema().dump(long_url)["long_url"]), 301


app.add_url_rule("/api/long-urls/", view_func=URLLongView.as_view("long-urls"))

app.add_url_rule(
    "/api/short-urls/<string:short_url>/", view_func=URLShortView.as_view("short-urls")
)

app.add_url_rule(
    "/<string:short_url>/", view_func=URLRedirectView.as_view("redirect-urls")
)
