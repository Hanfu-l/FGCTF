# Generated by Django 4.2.5 on 2024-06-10 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0002_notice'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='Keyvalue',
            field=models.CharField(default='123', max_length=255),
        ),
    ]
