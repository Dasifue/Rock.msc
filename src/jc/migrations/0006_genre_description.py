# Generated by Django 3.1.7 on 2021-06-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jc', '0005_auto_20210521_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='описание'),
        ),
    ]
