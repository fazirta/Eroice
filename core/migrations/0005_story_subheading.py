# Generated by Django 3.2.3 on 2021-07-05 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_story_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='subheading',
            field=models.CharField(max_length=200, null=True),
        ),
    ]