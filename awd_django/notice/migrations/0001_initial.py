# Generated by Django 4.2.5 on 2024-06-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('Description', models.CharField(max_length=255)),
                ('Visable', models.BooleanField(default=False)),
            ],
        ),
    ]
