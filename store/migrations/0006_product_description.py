# Generated by Django 4.1.6 on 2023-02-16 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]