# Generated by Django 3.2.6 on 2022-02-19 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='nurse',
            name='expertise_level',
            field=models.CharField(choices=[('1', 'Beginner'), ('2', 'Competent'), ('3', 'Expert')], default='1', max_length=2),
        ),
    ]