from django.db import models

# Create your models here.
class toplist (models.Model):
    movie_name = models.CharField(max_length=30)
    genre = models.CharField(max_length=15)
    pics_url = models.CharField(max_length=1000)
    year = models.IntegerField(default=20)
    date = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.movie_name
    