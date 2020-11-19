# Generated by Django 3.1.2 on 2020-11-15 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joblist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=1500)),
                ('education', models.CharField(blank=True, default='', max_length=1700, null=True)),
                ('experience', models.CharField(blank=True, default='', max_length=130, null=True)),
                ('industry', models.CharField(blank=True, default='', max_length=1200, null=True)),
                ('description', models.CharField(blank=True, default='', max_length=9000, null=True)),
                ('location', models.CharField(blank=True, default='', max_length=1200, null=True)),
                ('payrate', models.CharField(blank=True, default='', max_length=1500, null=True)),
                ('date', models.DateField(blank=True)),
                ('skills', models.CharField(blank=True, default='', max_length=1200, null=True)),
            ],
        ),
    ]
