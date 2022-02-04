# Generated by Django 4.0.1 on 2022-02-04 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bourse', '0004_alter_facture_client_alter_operation_voiture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Bourse.client'),
        ),
        migrations.AlterField(
            model_name='operation',
            name='voiture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voitures', to='Bourse.voiture'),
        ),
    ]
