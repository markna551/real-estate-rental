# Generated by Django 3.1 on 2020-10-27 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0002_auto_20201015_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='condo',
            old_name='condo_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='condo',
            old_name='condo_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_line_id',
            new_name='line_id',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='owner',
            old_name='owner_phone_number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='condo_name',
            new_name='condo',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='room_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='room_number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='owner_name',
            new_name='owner',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='room_title',
            new_name='title',
        ),
    ]