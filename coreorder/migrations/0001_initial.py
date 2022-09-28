# Generated by Django 4.1.1 on 2022-09-28 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=4)),
                ('academic_level', models.CharField(max_length=2)),
                ('paper_type', models.CharField(blank=True, max_length=5)),
                ('subject_area', models.CharField(max_length=5)),
                ('pages', models.PositiveIntegerField(blank=True, default=1)),
                ('words', models.PositiveIntegerField(blank=True, default=275)),
                ('prices', models.DecimalField(decimal_places=2, max_digits=6)),
                ('deadline', models.DateTimeField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.userprofile')),
            ],
            options={
                'verbose_name': 'order type (paper)',
                'verbose_name_plural': 'Order T',
            },
        ),
    ]
