# Generated by Django 4.0 on 2022-01-17 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_job',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='myapp.job_det'),
        ),
        migrations.AlterField(
            model_name='apply_job',
            name='jobappid',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='apply_job',
            name='reason',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='job_det',
            name='jobid',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='resume',
            name='resid',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]