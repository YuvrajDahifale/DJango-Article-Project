# Generated by Django 5.1 on 2024-10-07 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMediaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
