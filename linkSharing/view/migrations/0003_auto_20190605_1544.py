# Generated by Django 2.2.2 on 2019-06-05 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0002_auto_20190605_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='link',
            new_name='link_name',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='name',
            new_name='link_text',
        ),
    ]
