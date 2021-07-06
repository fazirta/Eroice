from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Genre(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Story(models.Model):
    user = models.ForeignKey(Profile, null=True, on_delete= models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    story = models.TextField(null=True)
    genre = models.ManyToManyField(Genre, blank=False)

    def __str__(self):
        return self.title
    
    def thumbnail_text(self):
        return self.story[:90]
    
    def thumbnail_genre(self):
        try:
            return self.genre.all()[0]
        except:
            return ''

class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)