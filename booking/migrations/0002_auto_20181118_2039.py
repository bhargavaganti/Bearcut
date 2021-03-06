# Generated by Django 2.1.3 on 2018-11-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='payment_type',
            field=models.CharField(choices=[('cash', 'CASH'), ('credit_card', 'CREDIT CARD')], default='CASH', max_length=10),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('pending', 'PENDING'), ('paid', 'PAID')], default='PENDING', max_length=10),
        ),
    ]
