# Generated by Django 2.1.7 on 2019-02-14 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='hargadiskon',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
