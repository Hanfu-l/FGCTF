# Generated by Django 4.2.5 on 2023-10-07 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0006_topic_sshname_topic_sshpassword'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='imagename',
        ),
    ]
