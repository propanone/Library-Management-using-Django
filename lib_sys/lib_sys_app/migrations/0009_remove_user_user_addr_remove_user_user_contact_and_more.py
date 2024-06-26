# Generated by Django 5.0.6 on 2024-06-11 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_sys_app', '0008_rename_userpassword_user_user_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_addr',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_contact',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_fullname',
        ),
        migrations.AddField(
            model_name='user',
            name='user_firstname',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_lastname',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
    ]
