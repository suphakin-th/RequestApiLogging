from django.db import models
from django.conf import settings

class RequestLog(models.Model):
    account = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    method = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    payload = models.TextField(blank=True, default='{}')
    status_code = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)