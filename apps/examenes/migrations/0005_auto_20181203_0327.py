# Generated by Django 2.1.2 on 2018-12-03 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0004_auto_20181203_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examenfisico',
            name='imagen',
            field=models.ImageField(upload_to='examenes'),
        ),
    ]