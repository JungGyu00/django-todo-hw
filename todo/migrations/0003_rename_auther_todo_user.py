# Generated by Django 4.2.5 on 2023-09-07 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_content_alter_todo_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='auther',
            new_name='user',
        ),
    ]
