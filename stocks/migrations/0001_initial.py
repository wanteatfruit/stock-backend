# Generated by Django 4.0.6 on 2022-07-26 05:53

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AAPL',
            fields=[
                ('Date', models.CharField(max_length=10, primary_key=sqlalchemy.sql.expression.true, serialize=False)),
                ('High', models.FloatField(null=sqlalchemy.sql.expression.true)),
                ('Low', models.FloatField(null=sqlalchemy.sql.expression.true)),
                ('Open', models.FloatField(null=sqlalchemy.sql.expression.true)),
                ('Close', models.FloatField(null=sqlalchemy.sql.expression.true)),
                ('Volume', models.FloatField(null=sqlalchemy.sql.expression.true)),
                ('Adj_Close', models.FloatField(null=sqlalchemy.sql.expression.true)),
                ('Predicted', models.FloatField(null=sqlalchemy.sql.expression.true)),
            ],
        ),
        migrations.CreateModel(
            name='ABBV',
            fields=[
                ('Date', models.CharField(max_length=10, primary_key=sqlalchemy.sql.expression.true, serialize=False)),
                ('High', models.FloatField(null=sqlalchemy.sql.expression.true)),
                ('Low', models.FloatField(null=sqlalchemy.sql.expression.true)),
                ('Open', models.FloatField(null=sqlalchemy.sql.expression.true)),
                ('Close', models.FloatField(null=sqlalchemy.sql.expression.true)),
                ('Volume', models.FloatField(null=sqlalchemy.sql.expression.true)),
                ('Adj_Close', models.FloatField(null=sqlalchemy.sql.expression.true)),
                ('Predicted', models.FloatField(null=sqlalchemy.sql.expression.true)),
            ],
        ),
    ]
