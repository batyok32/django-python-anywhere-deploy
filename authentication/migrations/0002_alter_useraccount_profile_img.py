# Generated by Django 3.2 on 2021-07-27 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='profile_img',
            field=models.ImageField(blank=True, default='default-icon.jpg', upload_to='users/%Y/%m/%d'),
        ),
    ]