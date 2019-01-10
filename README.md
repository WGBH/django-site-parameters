# Site Parameters

Site Parameters is a simple Django app to store customized site-level content, so that it can be maintained from the Admin 
by content managers. 

There are several models, each corresponding to a generic data type (e.g., text, images, URLs, etc.).  All data are available to all templates through a context processor.

As an example, you can have your site's copyright message as a SiteParameterString object rather than hard-coding it into a global footer template.   Or, you can upload a "site canonical image" that would be used as a placeholder in situations where an image in a template isn't available.  

In addition, you can also create site-wide navigation menus, and manage your site's list of social networks.

Detailed documentation is in the "docs" directory.

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


## Creating Site Parameters



## Using Site Parameters

Each parameter is loaded into the global context, making it available to every template.
They're loaded into dictionaries by each parameter type, e.g.:

    ```
	{{ site.parameter_string.my_cool_string }}
    ```
