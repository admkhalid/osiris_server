# Generated by Django 2.2.10 on 2020-03-07 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='x_co_ord',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
        migrations.AlterField(
            model_name='hub',
            name='y_co_ord',
            field=models.DecimalField(decimal_places=6, max_digits=9),
        ),
    ]
