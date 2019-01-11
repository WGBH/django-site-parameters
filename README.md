# Site Parameters

Site Parameters is a simple Django app to store customized site-level content, so that it can be maintained from the Admin 
by content managers. 

This includes:

* Basic "key, value" settings for common data types;
* Simple Navigation menus;
* Management of Social Media locations for the site.

All data are available to all templates through a context processor.

As an example, you can have your site's copyright message as a SiteParameterString object rather than hard-coding it into a global footer template.   Or, you can upload a "site canonical image" that would be used as a placeholder in situations where an image in a template isn't available.  

## Quick start

1. Add "site_parameters" to your INSTALLED_APPS setting like this::

    ```
    INSTALLED_APPS = [
        ...
        'site_parameters',
    ]
    ```

2. Add the context_processors to the system context_processors in the settings file like this::

    ```
    TEMPLATES = [
        {
                ...
                'OPTIONS': {
                        'context_processors': [
                                ...
                                'site_parameters.context_processors.get_custom_site_parameters',
                        ]
                        ...
                },
                ...
        }
    ]
    ```

3. Run `python manage.py migrate` to create the database tables.

4. Start the development server and visit `http://127.0.0.1:8000/admin/`
   to see the available models.


## Basic Site Parameters

You can add site parameters of the following types:

* Integers
* Strings
* Text blocks
* URLs
* Switches (booleans)
* Images

(At present, there's no Markdown or HTML support as both of these would require other components to be installed.)

In general, each has the following fields:

* Title
* Slug (automatically generated from the title, but can be over-ridden)
* Value

The title (for the most part) is just to make it easy to remember what the parameter is for (although it can be used in templates, etc. in the "regular" way).   

The slug is what's used in the global context for all templates.  Any hyphens are converted to underscores.   So if you have a Site: String with:

* title = "Copyright Notice"
* slug = "copyright-notice", and 
* value = "2019 Skepsis Interplanetary"

then you can use `{{ site_parameter_string.copyright_notice }}` in any template.

## Social Media

The Social Media model holds information about your site's external social media pages.  This is a convenience for being able 
to, e.g., manage lists of social media icons on pages, easily add or delete them as new services emerge and become popular, etc.

Each of the items in the Social Media list have a field to enter an SVG icon.  

The "Order in List" field handles ordering.

The "Available" field handles which items will be shown on the site.   

In templates, you can access the information from `{{ global_social_media_dict.slug }}`.

## Navigation

Navigation Menus are constructed by assembling sets of Navigation Items.  You can have as Navigation Menus as you need.

_If you are also using Django CMS_: the URL Slug field can be used to reference CMS Page objects.  Otherwise you can put in a root-relative URL in the  Internal Link field.

The ordered list of navigation items can be accessed in a template from the context name `global_nav_ + slug`, e.g., `global_nav_footer`.

