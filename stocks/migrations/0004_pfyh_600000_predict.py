# Generated by Django 4.0.6 on 2022-07-26 09:44

from django.db import migrations, models
import sqlalchemy.sql.expression


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_pfyh_600000'),
    ]

    operations = [
        migrations.AddField(
            model_name='pfyh_600000',
            name='Predict',
            field=models.FloatField(null=sqlalchemy.sql.expression.true),
            preserve_default=sqlalchemy.sql.expression.true,
        ),
    ]
