from django.db import models

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name 
        
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
class Score(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=100)
    score = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
