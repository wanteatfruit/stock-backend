# Generated by Django 4.0.6 on 2022-07-21 12:27

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_date', models.CharField(max_length=10)),
                ('price', models.FloatField(null=sqlalchemy.sql.expression.true)),
            ],
        ),
        migrations.CreateModel(
            name='B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_date', models.CharField(max_length=10)),
                ('price', models.FloatField(null=sqlalchemy.sql.expression.true)),
            ],
        ),
        migrations.CreateModel(
            name='C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_date', models.CharField(max_length=10)),
                ('price', models.FloatField(null=sqlalchemy.sql.expression.true)),
            ],
        ),
    ]
