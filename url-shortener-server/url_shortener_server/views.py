from flask import jsonify, request
from flask.views import MethodView
from url_shortener_db.models import URL
from url_shortener_server.serializers import URLSchema
from url_shortener_server.settings import app


class URLPost(MethodView):
    def post(self):
        serializer = URLSchema()
        urls = serializer.load(request.json)
        result = URL.add(**urls)
        return jsonify(serializer.dump(result)), 200


app.add_url_rule("/api/urls/", view_func=URLPost.as_view("urls"))
