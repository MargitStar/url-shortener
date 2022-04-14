from url_shortener_server import views
from url_shortener_server.base_routers import Pluggable

routes = [
    Pluggable("/api/long-urls/", views.URLLongView, "long-urls"),
    Pluggable("/api/short-urls/<string:short_url>/", views.URLShortView, "short-urls"),
    Pluggable("/<string:short_url>/", views.URLRedirectView, "redirect-urls"),
]
