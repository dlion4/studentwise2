# Generated by Django 4.1.1 on 2022-10-31 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to='account/<function user_directory_path at 0x0000029853AF2050>/'),
        ),
    ]
