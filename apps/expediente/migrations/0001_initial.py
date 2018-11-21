# Generated by Django 2.1.3 on 2018-11-12 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignoVital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatura', models.IntegerField(blank=True, null=True)),
                ('altura', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('presion_arterial', models.CharField(blank=True, max_length=7, null=True)),
                ('pulso_cardiaco', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]