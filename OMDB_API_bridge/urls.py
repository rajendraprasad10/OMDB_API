from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from movie_api.views import welcomehome, Search

# urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("movie_api.urls")),
    path("", welcomehome, name="index" ),
    path("search/", Search, name="search" )
]
