from django.db import models

class Certificate(models.Model):

    title = models.CharField(max_length=200)

    organization = models.CharField(max_length=150)

    image = models.ImageField(upload_to="certificates/")

    certificate_url = models.URLField(blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title