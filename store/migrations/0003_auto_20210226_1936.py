# Generated by Django 3.0.6 on 2021-02-26 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210226_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='finalprice',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invoice',
            name='toalprice',
            field=models.IntegerField(default=0),
        ),
    ]