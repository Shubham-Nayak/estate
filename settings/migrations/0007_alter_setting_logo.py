# Generated by Django 3.2.12 on 2023-09-10 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_auto_20230910_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='logo',
            field=models.ImageField(blank=True, upload_to='photos/img/'),
        ),
    ]
