from django.contrib import admin
from .abstract_admin import BaseParameterAdmin, BaseGenericStatusAdmin
from .models import  SiteParameterSwitch, SiteParameterURL, SiteParameterInteger, \
    SiteParameterText, SiteParameterString, SiteParameterImage, \
    SiteNavigationSectionItem, SiteNavigationSection, SiteSocialNetwork

class SiteNavigationSectionItemInline(admin.StackedInline):
    model = SiteNavigationSectionItem
    extra = 0
    ordering = ['-order_in_menu']
    fieldsets = (
        (None, 
            { 
                'fields': (
                    ('title', 'order_in_menu'),
                ),
            },
        ),
        ('Overall', 
            { 
                'fields': ( 'url_slug', 'internal_url', 'external_url', ),
                'description': "If this is a listing page from an apphook, put the \"name\" value from the urls.py file in the URL Slug field and leave External URL blank. Otherwise either put the partial URL in the Internal URL field (e.g., \'/about\'), or the complete URL in the external URL field."
            },
        ),
    )

class SiteNavigationSectionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', )
    list_display_links = ('pk', 'title')
    prepopulated_fields = {"slug": ("title",)}
    inlines = [SiteNavigationSectionItemInline, ]
    fieldsets = (
        (None, { 'fields': ( ('title', 'slug'), 'available_globally', )}),
    )
    ordering = ['pk',]
    
class SiteNavigationSectionItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'url_slug', 'internal_url', 'external_url')
    list_display_links = ('pk', 'title')
    #list_filter = ['navigation_section', ]
    readonly_fields = ['date_created', 'date_modified']
    fieldsets = (
        (None, 
            { 
                'fields': (
                    ('pk', 'date_created', 'date_modified'),
                    ('title',),

                ),
            },
        ),
        ('Overall', 
            { 
                'fields': ( 'url_slug', 'internal_url', 'external_url', ),
                'description': "If this is a listing page from an apphook, put the \"name\" value from the urls.py file in the URL Slug field and leave External URL blank. Otherwise either put the partial URL in the Internal URL field (e.g., \'/about\'), or the complete URL in the external URL field."
            },
        ),
    )
      
class SiteParameterSwitchAdmin(BaseParameterAdmin):
    pass

class SiteParameterURLAdmin(BaseParameterAdmin):
    fieldsets = (
        (None, 
            { 
                'fields': (
                    ('pk', 'date_created', 'date_modified'),
                    ('title', 'slug'),
                    ('value', 'new_window')
                ),
            },
        ),
    )
    
class SiteParameterIntegerAdmin(BaseParameterAdmin):
    pass
    
class SiteParameterTextAdmin(BaseParameterAdmin): 
    pass
    
class SiteParameterStringAdmin(BaseParameterAdmin):
    pass
    
class SiteParameterImageAdmin(BaseParameterAdmin):
    exclude = ['image_height', 'image_width', 'image_ppoi']

class SiteSocialNetworkAdmin(BaseGenericStatusAdmin):
    prepopulated_fields = {"slug": ("service",)}
    list_display = ['pk','service','available', 'url', 'order_in_list']
    list_display_links = ('pk', 'service')
    ordering = ('order_in_list',)
    readonly_fields = ('date_created', 'date_modified', 'pk')
    actions = ['make_available', 'make_unavailable']

    fieldsets = [
        (None, 
            {
                'fields': (
                    ('pk', 'available', 'date_created', 'date_modified'),
                    ('service', 'slug'),
                    ('title_on_service', ),
                    ('url',),
                    ('order_in_list',),
                )
            },
        ),
        ('Icon',
            {
                'fields': (
                    ('svg_path',),
                ),
                'classes': ('collapse',)
            },
        ),
    ]
    
    def get_readonly_fields(self, request, obj=None):
        if obj and not request.user.is_superuser: # editing an existing object
            return self.readonly_fields + ('svg_path',)
        return self.readonly_fields
        
admin.site.register(SiteNavigationSection, SiteNavigationSectionAdmin)
admin.site.register(SiteParameterSwitch, SiteParameterSwitchAdmin)
admin.site.register(SiteParameterURL, SiteParameterURLAdmin)
admin.site.register(SiteParameterInteger, SiteParameterIntegerAdmin)
admin.site.register(SiteParameterText, SiteParameterTextAdmin)
admin.site.register(SiteParameterString, SiteParameterStringAdmin)
admin.site.register(SiteParameterImage, SiteParameterImageAdmin)
admin.site.register(SiteSocialNetwork, SiteSocialNetworkAdmin)