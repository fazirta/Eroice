# Generated by Django 3.2.3 on 2021-07-05 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_story_subheading'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='subheading',
        ),
        migrations.AddField(
            model_name='story',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='story',
            name='genre',
            field=models.ManyToManyField(to='core.Genre'),
        ),
    ]