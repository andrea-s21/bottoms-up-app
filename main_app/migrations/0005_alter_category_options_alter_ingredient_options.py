# Generated by Django 4.0.2 on 2022-02-16 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_category_drink_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'ingredient', 'verbose_name_plural': 'ingredients'},
        ),
    ]