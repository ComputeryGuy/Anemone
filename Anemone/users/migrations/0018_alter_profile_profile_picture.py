# Generated by Django 4.1.1 on 2022-11-30 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_merge_20221129_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/logo-round.jpg', null=True, upload_to='images/'),
        ),
    ]
