# Generated by Django 3.0.3 on 2020-05-01 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_post_featured'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='categories',
        ),
    ]
