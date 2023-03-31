from django.contrib import admin
from .models import *

admin.site.register(GeneralUser)
admin.site.register(SubUser)
admin.site.register(EditImage)
admin.site.register(CategoriesNews)
admin.site.register(News)

# Register your models here.
