# Generated by Django 3.0.6 on 2021-03-01 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_invoicepdf_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoicepdf',
            old_name='pdf',
            new_name='pdff',
        ),
    ]
