# Generated by Django 3.2.3 on 2021-07-04 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_story_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='genre',
            field=models.ManyToManyField(blank=True, to='core.Genre'),
        ),
        migrations.AlterField(
            model_name='story',
            name='story',
            field=models.TextField(null=True),
        ),
    ]
