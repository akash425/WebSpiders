# Generated by Django 3.2 on 2021-05-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20210502_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
