from abc import ABC, abstractmethod
from importlib import import_module

from flask.views import View


class ImproperlyConfigured(Exception):
    pass


class BaseRouter(ABC):
    """https://github.com/thisissoon/Flask-Via/blob/master/flask_via/routers/__init__.py#L13"""

    @abstractmethod
    def __init__(self):
        raise NotImplementedError("__init__ must be overridden")

    @abstractmethod
    def add_to_app(self, app, **kwargs):
        raise NotImplementedError("add_to_app must be overridden")


class Pluggable(BaseRouter):
    """https://github.com/thisissoon/Flask-Via/blob/master/flask_via/routers/default.py#L137"""

    def __init__(self, url: str, view: View, endpoint: str, **kwargs):
        self.url = url
        self.view = view
        self.endpoint = endpoint
        self.kwargs = kwargs

    def add_to_app(self, app, **kwargs):
        url = self.url
        endpoint = self.endpoint

        #: If this route was included a url prefix may have been passed to the route
        if "url_prefix" in kwargs:
            url = kwargs["url_prefix"] + url

        #: If this route was included a endpoint prefix may have been passed to the route
        if "endpoint" in kwargs:
            endpoint = kwargs["endpoint"] + endpoint

        try:
            app.add_url_rule(url, view_func=self.view.as_view(endpoint), **self.kwargs)
        except AssertionError:
            # TODO: Log / Warn
            pass


class RoutesImporter:
    """https://github.com/thisissoon/Flask-Via/blob/master/flask_via/__init__.py#L12"""

    def include(self, routes_module, routes_name):
        # Import the module
        module = import_module(routes_module)

        # Get the routes from the module
        routes = getattr(module, routes_name)

        return routes

    def load(self, app, routes, **kwargs):
        for route in routes:
            route.add_to_app(app, **kwargs)


class Via(RoutesImporter):
    """https://github.com/thisissoon/Flask-Via"""

    def __init__(self, app=None, *args, **kwargs):
        if app:
            self.init_app(app, *args, **kwargs)

    def init_app(self, app, routes_module=None, routes_name=None, **kwargs):
        app.config.setdefault("VIA_ROUTES_MODULE", routes_module)
        app.config.setdefault("VIA_ROUTES_NAME", routes_name or "routes")

        if not app.config["VIA_ROUTES_MODULE"]:
            raise ImproperlyConfigured(
                "VIA_ROUTES_MODULE is not defined in application configuration."
            )

        routes_module = app.config["VIA_ROUTES_MODULE"]
        routes_name = app.config["VIA_ROUTES_NAME"]

        # Get the routes
        routes = self.include(routes_module, routes_name)

        # Load the routes
        self.load(app, routes, **kwargs)


def initialize_routes(app):
    via = Via()
    via.init_app(app, routes_module="url_shortener_server.routes")
