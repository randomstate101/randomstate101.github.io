# Generated by Django 2.2 on 2020-05-28 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tepsite', '0002_feedback_product'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Program',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='customer_name',
            new_name='intern_name',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='product',
            new_name='program',
        ),
    ]
