# Generated by Django 4.2.5 on 2023-10-08 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competition', '0011_alter_topic_external_alter_topic_interior'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='topic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='flags', to='competition.topic'),
            preserve_default=False,
        ),
    ]
