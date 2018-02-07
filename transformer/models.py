from django.db import models
from django.utils import timezone

class Document(models.Model):
	document = models.FileField(upload_to="uploads/")
	uploaded_at = models.DateTimeField(default=timezone.now)
	processed = models.BooleanField(default=False)
	result_url = models.CharField(max_length=100, default="")
