# Generated by Django 3.1.2 on 2020-11-15 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_scat'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblist',
            name='scat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.scat'),
            preserve_default=False,
        ),
    ]