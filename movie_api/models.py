from django.db import models

from django.db import models
from django.contrib.auth.models import User

# movie details model
class Movie(models.Model):
    Title = models.CharField(max_length=100)
    Year = models.CharField(max_length=100)
    Rated = models.CharField(max_length=100)
    Released = models.CharField(max_length=100)
    Genre = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.Title} (id: {self.id})"

# Rating details model
class Rating(models.Model):
    Source = models.CharField(max_length=100)
    Value = models.CharField(max_length=100)
    Movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="Ratings")


    def __str__(self):
        return f"Rating from {self.Source} to {self.Movie.Title})"

# comment model creations
class Comment(models.Model):
    comment_body = models.CharField(max_length=100)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="Comments")

    def __str__(self):
        return f" Comment for {self.movie_id} (id: {self.movie_id.id}): {self.comment_body}"
