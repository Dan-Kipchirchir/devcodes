# Generated by Django 3.0.6 on 2020-06-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='profilepic',
            field=models.FileField(upload_to=''),
        ),
    ]
