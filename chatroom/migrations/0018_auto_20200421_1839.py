# Generated by Django 3.0.3 on 2020-04-21 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
        ('chatroom', '0017_merge_20200420_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmodel',
            name='bell_seen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='chatmodel',
            name='r1uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_user', to='signup.Signup'),
        ),
        migrations.AlterField(
            model_name='chatmodel',
            name='r2uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_user', to='signup.Signup'),
        ),
    ]
