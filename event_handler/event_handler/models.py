from django.db import models

'''
This creates the model we will use to define a valid JSON request.
We use DateTimeField() to autoformat in the YYYY-MM-DD HH:MM:ss, we mark it as db_index since this is what we will use to look up entries.
The rest are text fields.
'''
class EventHandler(models.Model):
    event_type = models.TextField()
    mitre_threat_no = models.TextField()
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=False, db_index=True)
