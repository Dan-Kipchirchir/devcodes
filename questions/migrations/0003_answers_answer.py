# Generated by Django 3.0.3 on 2020-04-18 18:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20200418_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='answer',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
