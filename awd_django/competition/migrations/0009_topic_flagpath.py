# Generated by Django 4.2.5 on 2023-10-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0008_topic_interior_topic_interiorpath_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='flagpath',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
