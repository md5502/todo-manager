# Generated by Django 4.2.5 on 2023-09-10 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='goal',
            field=models.ManyToManyField(blank=True, to='tasks.goal'),
        ),
    ]