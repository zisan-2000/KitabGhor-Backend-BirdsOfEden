# Generated by Django 5.0.4 on 2024-07-13 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_product_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('books_count', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='writers/')),
            ],
        ),
    ]
