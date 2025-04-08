from djongo import models
from djongo.models.fields import ObjectIdField
from bson import ObjectId

class User(models.Model):
    id = ObjectIdField(primary_key=True)  # Change primary key to ObjectIdField
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()

class Team(models.Model):
    id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)  # Use ObjectId-compatible field
    name = models.CharField(max_length=255)
    members = models.ArrayField(model_container=User)  # Reference updated User model

class Activity(models.Model):
    id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)  # Use ObjectId-compatible field
    user = models.ForeignKey(User, on_delete=models.CASCADE, to_field='id')  # Ensure compatibility with ObjectId
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    id = models.CharField(max_length=24, default=lambda: str(ObjectId()), primary_key=True)  # Use ObjectId-compatible field
    team = models.ForeignKey(Team, on_delete=models.CASCADE, to_field='id')  # Ensure compatibility with ObjectId
    score = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()