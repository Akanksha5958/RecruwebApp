# Generated by Django 3.2.6 on 2022-01-24 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_apply_job_comemail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply_job',
            name='comemail',
        ),
    ]