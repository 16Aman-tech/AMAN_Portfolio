from django.db import models


class Profile(models.Model):

    name = models.CharField(max_length=100)

    role = models.CharField(max_length=150)

    bio = models.TextField()

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    location = models.CharField(max_length=100)

    github = models.URLField(blank=True)

    linkedin = models.URLField(blank=True)

    resume = models.FileField(upload_to="resume/")

    image = models.ImageField(upload_to="profile/")

    def __str__(self):
        return self.name