# Generated by Django 5.1.3 on 2024-11-19 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermercado', '0002_categoriaproducto_product_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=50),
        ),
    ]
