# Generated by Django 4.2 on 2024-08-23 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_like_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='products.hashtag'),
        ),
    ]
