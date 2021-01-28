# Generated by Django 3.1.5 on 2021-01-28 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advert_title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Наименование')),
                ('advert_slug', models.SlugField(unique=True, verbose_name='ЧПУ')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес дома')),
                ('rooms', models.IntegerField(verbose_name='Количество комнат')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('area', models.IntegerField(verbose_name='Общая площадь')),
                ('year', models.IntegerField(verbose_name='Год постройки')),
                ('building_type', models.CharField(choices=[('0', '----'), ('brick', 'кирпичный'), ('monolithic', 'монолитный'), ('wooden', 'деревянный'), ('aerated_concrete', 'газобетонный блок'), ('foam_concrete', 'пенобетонный блок')], default=None, max_length=30, verbose_name='Тип дома')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=100)),
                ('category_slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Категорию',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('advert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.advert')),
                ('floors', models.IntegerField(default=1, verbose_name='Этажность дома')),
                ('apartment_floor', models.IntegerField(default=1, verbose_name='Номер этажа')),
            ],
            options={
                'verbose_name': 'Квартиру',
                'verbose_name_plural': 'Квартиры',
            },
            bases=('main.advert',),
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('advert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.advert')),
                ('garage', models.BooleanField(default=False, verbose_name='Гараж')),
                ('plot', models.FloatField(default=0.0, verbose_name='Участок')),
            ],
            options={
                'verbose_name': 'Дом',
                'verbose_name_plural': 'Дома',
            },
            bases=('main.advert',),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_type', models.CharField(choices=[('realtor', 'риелтор'), ('company', 'агентство'), ('developer', 'застройщик'), ('owner', 'собственник')], default=None, max_length=20)),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Клиента',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.AddField(
            model_name='advert',
            name='advert_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='advert',
            name='advert_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец объявления'),
        ),
    ]
