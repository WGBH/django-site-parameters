# Generated by Django 2.1.5 on 2019-01-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_parameters', '0002_sitesocialnetwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesocialnetwork',
            name='title_on_service',
            field=models.CharField(help_text='The page title used at the service', max_length=250, verbose_name='Page Title'),
        ),
        migrations.AlterField(
            model_name='sitesocialnetwork',
            name='url',
            field=models.URLField(help_text="The URL of this site's page on the service.", max_length=250, verbose_name='URL'),
        ),
    ]
