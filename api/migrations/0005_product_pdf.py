# Generated by Django 5.0.4 on 2024-07-10 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_product_publication_product_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='products/pdfs/'),
        ),
    ]
