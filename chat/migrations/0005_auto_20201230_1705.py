# Generated by Django 3.1.4 on 2020-12-30 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0004_auto_20201226_2214"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatroom",
            name="audio_invite_url",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="chatroom",
            name="text_invite_url",
            field=models.URLField(blank=True),
        ),
    ]
