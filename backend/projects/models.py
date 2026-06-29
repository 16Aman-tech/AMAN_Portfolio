from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to="projects/")

    short_description = models.TextField()

    tech_stack = models.CharField(max_length=300)

    github = models.URLField(blank=True)

    live_demo = models.URLField(blank=True)

    featured = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0)

    created_at = models.DateField()

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title