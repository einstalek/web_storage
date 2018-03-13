from django.db import models
from django.utils import timezone
from datetime import datetime


class Document(models.Model):
    document = models.FileField(upload_to="videos/")
    uploaded_at = models.DateTimeField(default=timezone.now)
    processed = models.BooleanField(default=False)
    result_url = models.CharField(max_length=100, default="")
    config_start = models.TimeField(default=datetime.strptime('00:00:00', "%H:%M:%S"))
    config_end = models.TimeField(default=datetime.strptime('00:00:01', "%H:%M:%S"))
    num_machines = models.IntegerField(default=0)