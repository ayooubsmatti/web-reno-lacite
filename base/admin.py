from django.contrib import admin

# Register your models here.
from .models import Service,Client,DemendeUnAppel

# Register your models here.
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(DemendeUnAppel)