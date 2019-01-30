from django.conf import settings
from .models import SiteNavigationSection, SiteNavigationSectionItem, \
    SiteParameterImage, SiteParameterString, SiteParameterText, SiteParameterURL, \
    SiteParameterInteger, SiteParameterSwitch, SiteSocialNetwork

def get_custom_site_parameters(request):
    global_items = {}

    
    #### NAVS AND MENUS
    # This is based on the SiteNavigationSection model, which is basically a sub-menu of items grouped somewhere on a page.
    #   For WC2, there are two header Sections ("top" and "main")
    #   There are also THREE footer Sections ("left", "middle", and "right")
    #
    # Since you can presumably add more of these in different places, I've made the setting of the context variable generic;
    # the variable name is 'global_nav_' + the slug of the navigation menu.
    #
    navs = SiteNavigationSection.objects.filter(available_globally=True)
    for nav in navs:
        nav_items = SiteNavigationSectionItem.objects.filter(navigation_menu__slug=nav.slug).filter(order_in_menu__gt=0).order_by('-order_in_menu')
        key = 'global_nav_' + nav.slug.replace('-','_')
        global_items[key] = nav_items

    #########################################
    # GLOBAL STRINGS
    #       This are set in the global context with keys of site_parameter_string.string_slug_with_underscores_in_place_of_hyphens
    #
    #########################################
    try:
        site_strings = SiteParameterString.objects.all()
        d = {}
        for s in site_strings:
            d[s.slug.replace('-', '_')] = s.value
        global_items['site_parameter_string'] = d
    except:
        global_items['site_parameter_string'] = None
    
    ##########################################
    # GLOBAL IMAGES
    #
    ##########################################
    the_icons = SiteParameterImage.objects.all()
    for icon in the_icons:
        tag = icon.slug.replace('-','_')
        #if tag == 'pbs_passport_icon':
        #    tag = 'passport_icon'
        if tag == 'default-canonical-image':
            global_items['default_canonical_image'] = icon.value
        global_items[tag] = icon.value
       
    ##########################################
    # GLOBAL TEXTS
    #   These are like Strings above, except they COME OUT AS HTML.
    ########################################## 
    site_texts = SiteParameterText.objects.all()
    d = {}
    for text in site_texts:
        d[text.slug.replace('-','_')] = text.value
    global_items['site_parameter_texts'] = d
    
    ##########################################
    # GLOBAL NUMBERS
    ########################################## 
    site_numbers = SiteParameterInteger.objects.all()
    d = {}
    for number in site_numbers:
        d[number.slug.replace('-','_')] = number.value
    global_items['site_parameter_numbers'] = d
    
    ##########################################
    # GLOBAL SWITCHES
    ########################################## 
    site_switches = SiteParameterSwitch.objects.all()
    d = {}
    for sw in site_switches:
        d[sw.slug.replace('-', '_')] = sw.value
    global_items['site_parameter_switches'] = d
    
    ##########################################
    # GLOBAL EXTERNAL URL
    ########################################## 
    site_external_urls = SiteParameterURL.objects.all()
    d = {}
    for url in site_external_urls:
        d[url.slug.replace('-','_')] = url
    global_items['external_site'] = d

    ###### SOCIAL MEDIA THINGS    
    # Get the social network items
    social_networks = SiteSocialNetwork.objects.filter(available=True).order_by('order_in_list')
    global_items['global_social_media'] = social_networks
    social_media = {}
    for network in social_networks:
        social_media[network.slug] = network
    global_items['global_social_media_dict'] = social_media
    
    try:
        default_social_media_description = SiteParameterString.objects.get(slug='social-media-default-description')
        global_items['default_social_media_description'] = default_social_media_description.value
    except:
        global_items['default_social_media_description'] = 'Site Social Media'

    return global_items