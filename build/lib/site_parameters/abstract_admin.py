from django.contrib import admin, messages

class BaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
    class Meta:
        abstract = True
        
class BaseVocabAdmin(BaseAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('pk', 'title', 'slug', 'available')
    list_display_links = ('pk', 'title')
    ordering = ('slug',)
    search_fields = ['title',]
    readonly_fields = ('date_created', 'date_modified', 'pk')

    fieldsets = (
        (None, 
            { 
                'fields': (
                    ('pk', 'available', 'date_created', 'date_modified'),
                    ('title', 'slug'),
                ),
            },
        ),
    )
    
    class Meta:
        abstract = True
        
class BaseStatusAdmin(admin.ModelAdmin):
    actions = ['make_available', 'make_unavailable']
    
    def make_available(self, request, queryset):
        number_made_available = queryset.update(available=True)
        self.message_user(request, '%d page(s) made AVAILABLE' % number_made_available, level=messages.SUCCESS)
    make_available.short_description = 'Make items AVAILABLE'
        
    def make_unavailable(self, request, queryset):
        number_taken_offline = queryset.update(available = False)
        self.message_user(request, '%d page(s) made UNAVAILABLE.' % number_taken_offline, level=messages.SUCCESS)
    make_unavailable.short_description = 'Make items UNAVAILABLE'
    
    def get_actions(self, request):
        actions = super(BaseStatusAdmin, self).get_actions(request)
        if 'delete_selected' in actions.keys():
            del actions['delete_selected']
        return actions
        
    class Meta:
        abstract = True
        
class BaseParameterAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('pk', 'title', 'slug',  'value')
    list_display_links = ('pk', 'title')
    ordering = ('slug',)
    search_fields = ['title',]
    readonly_fields = ['date_created', 'date_modified', 'pk']

    fieldsets = (
        (None, 
            { 
                'fields': (
                    ('pk', 'date_created', 'date_modified'),
                    ('title', 'slug'),
                    ('value',)
                ),
            },
        ),
    )
    
    class Meta:
        abstract = True
        
# THE DIFFERENCE BETWEEN BaseStatusAdmin and BaseGenericStatusAdmin is that the latter has a slug field, while the former does not.
class BaseGenericStatusAdmin(BaseAdmin, BaseStatusAdmin):
    pass
    
    class Meta:
        abstract = True