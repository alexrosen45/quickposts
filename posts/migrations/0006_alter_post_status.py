# Generated by Django 4.1.5 on 2023-01-22 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.TextField(default='pending', null=True),
        ),
    ]