# Generated by Django 3.1.2 on 2020-11-15 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_ecat'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblist',
            name='ecat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.ecat'),
            preserve_default=False,
        ),
    ]
