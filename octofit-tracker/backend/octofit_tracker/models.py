from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    # Additional fields...

class Team(models.Model):
    name = models.CharField(max_length=100)
    # Additional fields...

class Activity(models.Model):
    description = models.TextField()
    # Additional fields...

class Leaderboard(models.Model):
    rank = models.IntegerField()
    # Additional fields...

class Workout(models.Model):
    type = models.CharField(max_length=100)
    # Additional fields...
