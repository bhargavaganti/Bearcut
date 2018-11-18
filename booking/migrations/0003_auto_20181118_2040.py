# Generated by Django 2.1.3 on 2018-11-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20181118_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='payment_type',
            field=models.CharField(choices=[('cash', 'CASH'), ('credit_card', 'CREDIT CARD')], default='cash', max_length=10),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('pending', 'PENDING'), ('paid', 'PAID')], default='pending', max_length=10),
        ),
    ]