# Generated by Django 3.2.6 on 2021-12-30 20:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_adreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='adreview',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adreview',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
