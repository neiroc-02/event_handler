from django.db import models

class EventHandler(models.Model):
    event_type = models.TextField()
    mitre_threat_no = models.TextField()
    description = models.TextField()
    timestamp = models.TextField()
