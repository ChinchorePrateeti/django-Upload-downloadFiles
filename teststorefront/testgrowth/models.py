from django.db import models

# Create your models here.
class uploadTask(models.Model):
    ids = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=300)
    the_file = models.FileField(upload_to='')

    def __str__(self):
        return self.file_name
