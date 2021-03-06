# Generated by Django 2.1.5 on 2019-01-09 16:02

from django.db import migrations, models
import django.db.models.deletion
import site_parameters.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteNavigationSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('available_globally', models.BooleanField(default=True, help_text='Should this menu be available across the entire site?', verbose_name='Global Menu')),
            ],
            options={
                'verbose_name': 'Site Navigation Menu',
                'verbose_name_plural': 'Site Navigation Menus',
            },
        ),
        migrations.CreateModel(
            name='SiteNavigationSectionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('url_slug', models.CharField(blank=True, help_text='If an apphook listing page, the "name" value from the urls.py file. (You will need to ask a developer for this.)', max_length=100, null=True, verbose_name='URL Slug')),
                ('internal_url', models.CharField(blank=True, help_text="Use this for directly accessing an internal page with its partial URL: e.g., '/about'", max_length=100, null=True, verbose_name='Internal Link')),
                ('external_url', models.URLField(blank=True, help_text='If this is an external link, put the URL here', max_length=250, null=True, verbose_name='External URL')),
                ('order_in_menu', models.PositiveIntegerField(default=0, help_text='Order in Menu, if > 0, highest is shown first', verbose_name='Menu Order')),
                ('navigation_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='site_parameters.SiteNavigationSection')),
            ],
            options={
                'verbose_name': 'Navigation Item',
                'verbose_name_plural': 'Navigation Items',
            },
        ),
        migrations.CreateModel(
            name='SiteParameterImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('value', models.ImageField(height_field='image_height', help_text="This is 'image' in the template tag.", upload_to=site_parameters.models.get_upload_to, verbose_name='Image', width_field='image_width')),
                ('image_height', models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Height')),
                ('image_width', models.PositiveIntegerField(blank=True, null=True, verbose_name='Image Width')),
            ],
            options={
                'verbose_name': 'Site Image',
                'verbose_name_plural': 'Site Images',
            },
        ),
        migrations.CreateModel(
            name='SiteParameterInteger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('value', models.IntegerField(blank=True, help_text="This is 'number' in the template tag", null=True, verbose_name='Number')),
            ],
            options={
                'verbose_name': 'Numbered Parameter',
                'verbose_name_plural': 'Numbered Parameters',
            },
        ),
        migrations.CreateModel(
            name='SiteParameterString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('value', models.CharField(blank=True, help_text="This is 'string' in the template tag.", max_length=255, null=True, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Site String',
                'verbose_name_plural': 'Site Strings',
            },
        ),
        migrations.CreateModel(
            name='SiteParameterSwitch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('value', models.BooleanField(default=False, help_text="This is 'switch' in the template tag.", verbose_name='Switch')),
            ],
            options={
                'verbose_name': 'Site Switch',
                'verbose_name_plural': 'Site Swtiches',
            },
        ),
        migrations.CreateModel(
            name='SiteParameterText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('value', models.TextField(blank=True, help_text="This is 'text' in the template tag.", null=True, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Site Text Block',
                'verbose_name_plural': 'Site Text Blocks',
            },
        ),
        migrations.CreateModel(
            name='SiteParameterURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=120, unique=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('value', models.URLField(blank=True, help_text="This is 'url' in the template tag.", null=True, verbose_name='URL')),
                ('new_window', models.BooleanField(default=True, verbose_name='Opens New Browser Window')),
            ],
            options={
                'verbose_name': 'External Site URL',
                'verbose_name_plural': 'External Site URLs',
            },
        ),
    ]
