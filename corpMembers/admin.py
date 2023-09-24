from django.contrib import admin

# Register your models here.
from .models import Category, User,Contact, About, Gallery


class GalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}



admin.site.register(Category)
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Gallery, GalleryAdmin)

