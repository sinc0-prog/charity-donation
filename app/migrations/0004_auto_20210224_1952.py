# Generated by Django 2.2.6 on 2021-02-24 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Institution'),
        ),
    ]
