from django.db import models

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    percentage = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.degree