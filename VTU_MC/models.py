from django.db import models


# Create your models here.
class Pdf_mc(models.Model):
    name_m = models.CharField(max_length=40)
    pdf_m = models.FileField(upload_to='media/pdfs/', null=True, blank=True)
