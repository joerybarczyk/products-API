# Generated by Django 4.0.3 on 2022-03-31 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')])),
                ('text', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
