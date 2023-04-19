# Generated by Django 4.1.4 on 2022-12-26 06:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('status', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
