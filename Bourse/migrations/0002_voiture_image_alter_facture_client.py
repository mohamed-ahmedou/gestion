# Generated by Django 4.0.1 on 2022-01-23 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bourse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voiture',
            name='image',
            field=models.ImageField(null=True, upload_to='static/image'),
        ),
        migrations.AlterField(
            model_name='facture',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Bourse.client'),
        ),
    ]