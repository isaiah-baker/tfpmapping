# Generated by Django 2.2.2 on 2019-06-07 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0003_auto_20190605_1544'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='link_text',
            new_name='url',
        ),
    ]