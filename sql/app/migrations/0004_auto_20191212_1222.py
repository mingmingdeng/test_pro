# Generated by Django 2.2.6 on 2019-12-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191212_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='db_name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
