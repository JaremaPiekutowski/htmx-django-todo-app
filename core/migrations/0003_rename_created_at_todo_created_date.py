# Generated by Django 4.2.4 on 2024-05-18 11:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_todo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="created_at",
            new_name="created_date",
        ),
    ]