# Generated by Django 3.1.7 on 2021-03-04 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210304_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='description',
            field=models.TextField(),
        ),
    ]