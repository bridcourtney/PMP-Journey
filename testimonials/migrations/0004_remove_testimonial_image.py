# Generated by Django 3.1.5 on 2021-02-20 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0003_testimonial_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testimonial',
            name='image',
        ),
    ]
