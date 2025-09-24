from django.db import models
from django.contrib.auth.models import User

class GeneratedExamHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    num_versions = models.PositiveIntegerField()
    zip_file = models.FileField(upload_to='generated_zips/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.filename} ({self.created_at.date()})"
