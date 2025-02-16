# Generated by Django 4.2.5 on 2025-02-16 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('min_income', models.IntegerField()),
                ('max_income', models.IntegerField()),
                ('category', models.CharField(max_length=255)),
                ('link', models.URLField()),
            ],
        ),
    ]
