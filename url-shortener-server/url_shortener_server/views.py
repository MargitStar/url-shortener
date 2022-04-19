from flask import abort, jsonify, redirect, request
from flask.views import MethodView
from url_shortener_db.models import URL
from url_shortener_server.serializers import URLLongSchema, URLShortSchema


class URLLongView(MethodView):
    def post(self):
        url = URLLongSchema().load(request.json)
        result = URL.add(**url)
        return jsonify(URLShortSchema().dump(result)), 201


class BaseURLLogic:
    @staticmethod
    def get_short_url(short_url):
        long_url = URL.get_by_short_url(short_url=short_url)
        if not long_url:
            abort(
                404,
                description=f"Long url not found. Short url {short_url} does not exist!",
            )
        return long_url


class URLShortView(BaseURLLogic, MethodView):
    def get(self, short_url):
        long_url = self.get_short_url(short_url)
        return jsonify(URLLongSchema().dump(long_url)), 200


class URLRedirectView(BaseURLLogic, MethodView):
    def get(self, short_url):
        url = self.get_short_url(short_url)
        return redirect(url.long_url), 301
