# Generated by Django 3.0.7 on 2022-03-26 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20220324_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='value',
            field=models.FileField(upload_to='media'),
        ),
    ]
