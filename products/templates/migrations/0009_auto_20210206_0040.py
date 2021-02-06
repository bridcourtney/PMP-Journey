# Generated by Django 3.1.5 on 2021-02-06 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210206_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='book_type',
            field=models.CharField(blank=True, choices=[('Hardback', 'Hardback'), ('Kindle', 'Kindle'), ('Paperback', 'Paperback'), ('', '')], default='', max_length=254),
        ),
    ]
