# Generated by Django 4.0.2 on 2022-02-15 23:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_id', models.CharField(max_length=10)),
                ('drink_name', models.CharField(max_length=100)),
                ('drink_instructions', models.TextField(max_length=500)),
                ('drink_pic', models.CharField(max_length=100)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liquor_pref', models.CharField(choices=[('V', 'Vodka'), ('G', 'Gin'), ('R', 'Rum'), ('T', 'Tequila')], default='V', max_length=1, verbose_name='What is your preferred liquor?')),
                ('q1', models.CharField(choices=[('W', 'Work'), ('P', 'Play')], default='W', max_length=1, verbose_name='Was Today work or play?')),
                ('q2', models.CharField(choices=[('A', 'Adventurous'), ('C', 'Classic')], default='A', max_length=1, verbose_name='Are you feeling adventurous or classic?')),
                ('q3', models.CharField(choices=[('P', 'Pick-Me-Up'), ('R', 'Relaxation')], default='P', max_length=1, verbose_name='Do you need a pick-me-up or to relax?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(choices=[('1', 'drink_ingredient1'), ('2', 'drink_ingredient2'), ('3', 'drink_ingredient3'), ('4', 'drink_ingredient4'), ('5', 'drink_ingredient5'), ('6', 'drink_ingredient6'), ('7', 'drink_ingredient7'), ('8', 'drink_ingredient8')], default='1', max_length=50)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.drink')),
            ],
        ),
    ]
