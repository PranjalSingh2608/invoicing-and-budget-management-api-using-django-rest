# Generated by Django 4.1.5 on 2023-06-26 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0004_delete_invoiceitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='item_description',
            field=models.CharField(default='item description', max_length=200),
            preserve_default=False,
        ),
    ]
