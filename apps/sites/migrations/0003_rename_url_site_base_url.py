# Generated by Django 5.0.6 on 2024-06-02 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_site_redirect_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='url',
            new_name='base_url',
        ),
    ]
