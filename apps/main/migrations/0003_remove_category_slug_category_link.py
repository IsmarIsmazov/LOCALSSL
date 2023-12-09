# Generated by Django 4.2.7 on 2023-11-10 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='link',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
