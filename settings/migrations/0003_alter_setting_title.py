# Generated by Django 3.2.12 on 2023-09-10 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20230910_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='title',
            field=models.CharField(blank=True, default='MyApp | ', max_length=200),
        ),
    ]
