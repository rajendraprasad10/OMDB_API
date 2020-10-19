from django.conf.urls import url
from .views import MoviesView, CommentsView

# url for APIs viewing
urlpatterns = [
    url('movies', MoviesView.as_view(), name="MoviesView"),
    url('comments', CommentsView.as_view(), name="CommentsView"),

]
