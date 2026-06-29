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
    
class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.role} - {self.company}"