# Generated by Django 2.2.6 on 2019-12-13 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191212_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='db_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='instance',
            unique_together={('db_name', 'env')},
        ),
    ]
