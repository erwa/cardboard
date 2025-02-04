# Generated by Django 4.0.1 on 2022-01-06 23:08
from django.db import migrations
from django.template.defaultfilters import slugify
from django.conf import settings


def get_setting(settings, var):
    if hasattr(settings, var):
        return getattr(settings, var) or ""
    else:
        return ""


def add_settings(apps, schema_editor):
    Hunt = apps.get_model("hunts", "Hunt")
    HuntSettings = apps.get_model("hunts", "HuntSettings")
    for hunt in Hunt.objects.all():
        if not hasattr(hunt, "settings"):
            hunt_settings = HuntSettings(
                hunt=hunt,
                google_drive_folder_id=get_setting(
                    settings, "GOOGLE_DRIVE_HUNT_FOLDER_ID"
                ),
                google_sheets_template_file_id=get_setting(
                    settings, "GOOGLE_SHEETS_TEMPLATE_FILE_ID"
                ),
                google_drive_human_url=get_setting(
                    settings, "GOOGLE_HUMAN_DRIVE_HUNT_FOLDER_URL"
                ),
                discord_guild_id=get_setting(settings, "DISCORD_GUILD_ID"),
                discord_puzzle_announcements_channel_id=get_setting(
                    settings, "DISCORD_PUZZLE_ANNOUNCEMENTS_CHANNEL"
                ),
                discord_text_category=get_setting(settings, "DISCORD_TEXT_CATEGORY"),
                discord_voice_category=get_setting(settings, "DISCORD_VOICE_CATEGORY"),
                discord_archive_category=get_setting(
                    settings, "DISCORD_ARCHIVE_CATEGORY"
                ),
                discord_devs_role=get_setting(settings, "DISCORD_DEVS_ROLE"),
            )
            hunt_settings.save()


class Migration(migrations.Migration):

    dependencies = [
        ("hunts", "0007_huntsettings"),
    ]

    operations = [
        migrations.RunPython(
            add_settings,
            reverse_code=migrations.RunPython.noop,
        )
    ]
