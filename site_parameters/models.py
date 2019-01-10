from django.db import models
#from djangocms_text_ckeditor.fields import HTMLField
from django.utils.translation import ugettext_lazy as _
from .abstract_models import BaseTimeStampModel, BaseTitleModel, BaseSlugModel, BaseControlledVocabulary, BaseOrderedModel, BaseGenericModel

class AbstractSiteParameter(BaseTimeStampModel, BaseTitleModel, BaseSlugModel):
    """
    All site parameters, regardless of type have:
        date_created and date_modified,
        title and slug
    """
    pass
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.title

class SiteNavigationSection(BaseControlledVocabulary):
    """
    This model handles clusters of navigation items, e.g., parts of the header or footer,
    but they can also be other customized navs.
    
    Items in the navs needn't be monogamous.
    
    """
    available_globally = models.BooleanField (
        _('Global Menu'),
        default = True,
        help_text = 'Should this menu be available across the entire site?'
    )
    
    class Meta:
        verbose_name = 'Navigation Menu'
        verbose_name_plural = 'Navigation Menus'
    
    def __str__(self):
        return self.title

class SiteNavigationSectionItem(BaseTimeStampModel, BaseTitleModel):
    """
    APOLOGIA:
    
    If the same reference appears in >1 SiteNavigationSection instances,
    the you WILL have to make the slug unique.
    
    Sorry about that.
    
    RAD: 2018-Aug-23
    """
    url_slug = models.CharField (
        _('URL Slug'),
        max_length = 100,
        null = True, blank=True,
        help_text = 'If an apphook listing page, the \"name\" value from the urls.py file. (You will need to ask a developer for this.)'
    )
    internal_url = models.CharField (
        _('Internal Link'),
        max_length = 100,
        null = True, blank = True,
        help_text = 'Use this for directly accessing an internal page with its partial URL: e.g., \'/about\''
    )
    external_url = models.URLField (
        _('External URL'),
        max_length = 250,
        null = True, blank = True,
        help_text = 'If this is an external link, put the URL here'
    )
    
    navigation_menu = models.ForeignKey (
        SiteNavigationSection,
        related_name='menu_items',
        on_delete=models.CASCADE,  # required for Django 2.0
    )
    
    order_in_menu = models.PositiveIntegerField (
        _('Menu Order'),
        null = False, default = 0,
        help_text = 'Order in Menu, if > 0, highest is shown first'
    )
        
    class Meta:
        verbose_name = 'Navigation Menu Item'
        verbose_name_plural = 'Navigation Menu Items'
        
###################################### UNARY PARAMETERS BY TYPE #########################################################
        
class SiteParameterSwitch(AbstractSiteParameter):
    """
    Site Boolean, e.g., "show contact us on homepage"
    """
    value = models.BooleanField (
        _('Switch'),
        default = False,
        help_text = "This is \'switch\' in the template tag."
    )
    
    class Meta:
        verbose_name = 'Site: Switch'
        verbose_name_plural = 'Site: Swtiches'
        
    
class SiteParameterURL(AbstractSiteParameter):
    """
    Site URL, e.g. "pbs-url" could be "http://www.pbs.org/"
    """
    value = models.URLField (
        _('URL'),
        null = True,
        blank = True,
        help_text = "This is \'url\' in the template tag."
    )
    new_window = models.BooleanField (
        _('Opens New Browser Window'),
        default = True
    )
    
    class Meta:
        verbose_name = 'Site: URL Reference'
        verbose_name_plural = 'Site: URL References'
        
class SiteParameterInteger(AbstractSiteParameter):
    """
    Site Integer - this is good for things like establishing pagination limits, etc.
    """
    value = models.IntegerField (
        _('Number'),
        null = True,
        blank = True,
        help_text = 'This is \'number\' in the template tag'
    )
    
    class Meta:
        verbose_name = 'Site: Numbered Parameter'
        verbose_name_plural = 'Site: Numbered Parameters'
        
class SiteParameterText(AbstractSiteParameter):
    """
    Site Text - this might be some kind of global disclaimer message that appears in the 
    footer, but you want to be able to edit/change now and then.
    """
    value = models.TextField (
        _('Text'),
        null = True, 
        blank = True,
        help_text = "This is \'text\' in the template tag."
    )
    
    class Meta:
        verbose_name = 'Site: Text Block'
        verbose_name_plural = 'Site: Text Blocks'
    
class SiteParameterString(AbstractSiteParameter):
    """
    Site String - this is for global labels, e.g., "site-banner-text" = "Welcome to our website!"
    """
    value = models.CharField (
        _('Value'),
        max_length = 255,
        null = True,
        blank = True,
        help_text = "This is \'string\' in the template tag."
    )
    
    class Meta:
        verbose_name = 'Site: String'
        verbose_name_plural = 'Site: Strings'
    
def get_upload_to(instance, filename):
    return instance.get_upload_to_path(filename)
    
class SiteParameterImage(AbstractSiteParameter):
    """
    Site images.
    
        There are two that REALLY SHOULD BE DEFINED HERE.
        1) 'default-canonical-image' should be set to an image that everything else on the site falls back to,
            when another more-appropriate image can't be found.   Aspect ratio ~ 16:9 is a good idea.
        2) 'default-poster-image' ditto, but here, aspect ratio ~ 2:3 is a good idea.
    """
    value = models.ImageField (
        _('Image'),
        width_field='image_width', height_field='image_height',
        upload_to = get_upload_to,
        help_text = "This is \'image\' in the template tag."
    )
    image_height = models.PositiveIntegerField(
        'Image Height',
        blank=True,
        null=True
    )
    image_width = models.PositiveIntegerField(
        'Image Width',
        blank=True,
        null=True
    )
    
    class Meta:
        verbose_name = 'Site: Image'
        verbose_name_plural = 'Site: Images'
    
    def get_upload_to_path(instance, filename):
        return 'canonical_images/site/'+filename
        

class AbstractSocialNetwork(BaseGenericModel, BaseOrderedModel):
    service = models.CharField (
        _('Site Name'),
        max_length = 250,
        null = False,
        help_text = 'The name of the service (e.g., Facebook, YouTube)'
    )
    title_on_service = models.CharField (
        _('Page Title'),
        max_length = 250,
        null = False,
        help_text = 'The page title used at the service'
    )
    url = models.URLField (
        _('URL'),
        max_length = 250,
        null = False, 
        help_text = 'The URL of this site\'s page on the service.'
    )
    svg_path = models.TextField (
        _('SVG Path'),
        null = True, blank = True,
        # default = 'I need to put an SVG path here...'
        help_text = 'You need to be superuser to edit this.'
    )
    
    class Meta:
        verbose_name = 'Social Media Site'
        verbose_name_plural = 'Social Media Sites'
        abstract = True
    
    def __str__(self):
        return "%s (%s)" % (self.service, self.url)
        
class SiteSocialNetwork(AbstractSocialNetwork):
    pass