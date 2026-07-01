from django.db import models


class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} - {self.visited_at.strftime('%d %b %Y %H:%M')}"