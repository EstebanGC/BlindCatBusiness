# Generated by Django 4.2.1 on 2023-05-17 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('clientIdType', models.CharField(max_length=5)),
                ('clientId', models.CharField(max_length=20)),
                ('clientName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
                ('productPrice', models.IntegerField(default=0)),
                ('producQuantity', models.CharField(max_length=20)),
                ('stock', models.IntegerField(default=0)),
                ('minProduct', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('totalPrice', models.IntegerField()),
                ('buy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blindcatb.buy')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blindcatb.product')),
            ],
        ),
    ]
