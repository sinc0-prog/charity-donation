# Generated by Django 2.2.6 on 2021-02-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=255)),
                ('type_of', models.CharField(choices=[('fundacja', 'fundacja'), ('organizacja pozarządowa', 'organizacja pozarządowa'), ('zbiórka lokalna', 'zbiórka lokalna')], default='fundacja', max_length=64)),
                ('categories', models.ManyToManyField(to='app.Category')),
            ],
        ),
    ]
