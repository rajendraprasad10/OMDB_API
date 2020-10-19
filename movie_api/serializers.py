from rest_framework import serializers
from .models import Movie, Comment, Rating
from drf_writable_nested import WritableNestedModelSerializer

# rating API creation
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ("Source", "Value")

# movie details API creations
class MovieSerializer(WritableNestedModelSerializer):
    Ratings = RatingSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

# comment api creations
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
