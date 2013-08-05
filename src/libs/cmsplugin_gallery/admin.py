from inline_ordering.admin import OrderableStackedInline
import forms
import models
from django.contrib import admin

class ImageInline(OrderableStackedInline):
    
    model = models.Image
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'src':
            kwargs.pop('request', None)
            kwargs['widget'] = forms.AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageInline, self).formfield_for_dbfield(db_field, **kwargs)
class CategoryInline(OrderableStackedInline):
    model=models.GCategory

admin.site.register(models.Category, CategoryInline)