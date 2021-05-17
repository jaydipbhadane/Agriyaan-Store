# Generated by Django 3.0.6 on 2021-03-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_invoice_fullname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoicepdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=120)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdfs/')),
            ],
        ),
    ]