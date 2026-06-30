from django.db import models


class CodingProfile(models.Model):
    platform = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    profile_url = models.URLField()
    icon = models.ImageField(upload_to="coding/")
    stats = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.platform