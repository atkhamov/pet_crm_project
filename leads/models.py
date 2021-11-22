from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    # 'pass' indicates that we are going to take default 'first_name'
    # and 'last_name' fields from AbstractUser


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Here we don't need to create 'first_name' and 'last_name' kind
    # fields, as User model has them already. Therefore, we just need to
    # indicate the OneToOneField relationship, which ensures that
    # the user will become Agent automatically, and credentials
    # will get persisted in Agent model as well
