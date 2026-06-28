from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()
    icon = models.ImageField(upload_to="skills/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name