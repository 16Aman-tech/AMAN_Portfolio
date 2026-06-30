from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)

    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.title

