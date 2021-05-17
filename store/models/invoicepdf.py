from django.db import models
from io import BytesIO
from django.core.files import File
from Eshop.utils import render_to_pdf

class Invoicepdf(models.Model):
    mypdf = models.FileField(upload_to='pdfs/', null=True, blank=True)
