# Generated by Django 4.1.1 on 2022-09-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreorder', '0004_alter_ordertype_prices_alter_ordertype_subject_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertype',
            name='deadline',
            field=models.DateField(),
        ),
    ]