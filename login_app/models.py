from django.db import models

class Users(models.Model):
    userid = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)  # ⚠️ en producción usa hashing

    def __str__(self):
        return self.userid