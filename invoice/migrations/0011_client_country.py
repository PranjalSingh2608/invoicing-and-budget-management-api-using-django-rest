# Generated by Django 4.1.5 on 2023-06-26 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0010_client_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='country',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
