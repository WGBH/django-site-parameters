from django.db import models
from django.utils.translation import ugettext_lazy as _


################################################################################################### ABSTRACT STATUS CLASSES
###################################################################################################
class BaseGenericStatusModel(models.Model):
    available = models.BooleanField (
        _('Available'),
        null = False,
        default = True,
    )

    class Meta:
        abstract = True

################################################################################################### ABSTRACT SLUG/TITLE CLASSES
###################################################################################################
class BaseSlugModel(models.Model):
    slug = models.SlugField (
        unique = True,
        null = False,
        max_length = 120,
    )

    class Meta:
        abstract = True

class BaseTitleModel(models.Model):
    title = models.CharField (
        _('Title'),
        max_length = 200,
        null = False
    )

    class Meta:
        abstract = True


################################################################################################### ABSTRACT TIME STAMP CLASSES
###################################################################################################
class BaseTimeStampModel(models.Model):
    date_created = models.DateTimeField (
        _('Date Created'),
        auto_now_add = True
    )
    date_modified = models.DateTimeField (
        _('Last Updated'),
        auto_now = True
    )

    class Meta:
        abstract = True
        
###################################################################################################
################################################################################################### ABSTRACT ORDERED CLASSES
###################################################################################################
class BaseOrderedModel(models.Model):
    order_in_list = models.PositiveIntegerField (
        _('Order in List'),
        null = False,
        default = 0
    )

    class Meta:
        abstract = True
        


################################################################################################### COMBINED ABSTRACT CLASSES
###################################################################################################
class BaseGenericModel(BaseGenericStatusModel, BaseTimeStampModel, BaseSlugModel):

    class Meta:
        abstract = True


class BaseControlledVocabulary(BaseGenericStatusModel, BaseTimeStampModel, BaseTitleModel, BaseSlugModel):

    class Meta:
        abstract = True
