# Generated by Django 4.1.5 on 2023-02-02 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0004_alter_product_discription"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="size",
            field=models.CharField(blank=True, default="", max_length=10, null=True),
        ),
    ]
