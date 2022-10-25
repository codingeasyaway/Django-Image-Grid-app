from django.contrib import admin

# Register your models here.
from .models import Image, About, Contact

admin.site.site_header = 'Gull - Image Grid | Dashboard'
admin.site.register(Image)
admin.site.register(About)
admin.site.register(Contact)
