from flask import jsonify, redirect, request
from flask.views import MethodView
from url_shortener_db.models import URL
from url_shortener_server.serializers import URLLongSchema, URLShortSchema


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
        if not long_url:
            return {"detail": "Not Found"}, 404
        return redirect(URLLongSchema().dump(long_url).get("long_url")), 301
