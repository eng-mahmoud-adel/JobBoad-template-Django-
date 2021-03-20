# Generated by Django 3.1.7 on 2021-03-18 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_applyforjob'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyforjob',
            name='applied_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='applyforjob',
            name='job',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='job.job'),
        ),
    ]