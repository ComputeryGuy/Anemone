# Generated by Django 4.0.7 on 2022-10-04 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_bio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AlterField(
            model_name='profile',
            name='household',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
