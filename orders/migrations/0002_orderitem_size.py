# Generated by Django 3.2 on 2021-08-27 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='size',
            field=models.CharField(default='M', max_length=50),
            preserve_default=False,
        ),
    ]
