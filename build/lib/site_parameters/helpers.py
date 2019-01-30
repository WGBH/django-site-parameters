from .models import  SiteParameterSwitch, SiteParameterURL, SiteParameterInteger, \
    SiteParameterText, SiteParameterString, SiteParameterImage, \
    SiteNavigationSectionItem

### This is just a dict of models with keys.
PARAM_TYPES = {
    'switch': SiteParameterSwitch,
    'url': SiteParameterURL,
    'number': SiteParameterInteger,
    'text': SiteParameterText,
    'string': SiteParameterString,
    'image': SiteParameterImage
}

def find_site_parameter(slug=None, default=None, param_type=None):
    """
    Look up a site parameter by type and slug.
    If no type is given, all of them are searched.
    
    If the queryset is empty, then return the default value provided.
    
    Isn't that neat?   
    """
    if not slug: # why did you call me when you have nothing to say?
        return None
    if param_type: # faster
        try:
            item = PARAM_TYPES[param_type].objects.get(slug=slug)
            return item.value
        except:
            return default
    else: # slower
        for k in PARAM_TYPES.keys():
            try:
                item = PARAM_TYPES[param_type].objects.get(slug=slug)
                return item.value
            except:
                pass # try again
    # I couldn't find anything - sorry.
    return default
            