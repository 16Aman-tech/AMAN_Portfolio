from django.db import models


class Visitor(models.Model):

    ip_address = models.GenericIPAddressField()

    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f"{self.ip_address} - {self.visited_at.strftime('%d %b %Y %H:%M')}"


class ResumeDownload(models.Model):

    downloaded_at = models.DateTimeField(auto_now_add=True)

    ip_address = models.GenericIPAddressField()

    def __str__(self):

        return f"Resume Download - {self.downloaded_at.strftime('%d %b %Y %H:%M')}"