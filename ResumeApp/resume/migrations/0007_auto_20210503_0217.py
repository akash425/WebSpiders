# Generated by Django 3.2 on 2021-05-02 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_alter_resume_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='first_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='last_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]