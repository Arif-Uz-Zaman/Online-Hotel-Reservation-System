from django.contrib import admin

from .models import District, profile,division,Blood

# Register your models here.
admin.site.register(profile)
admin.site.register(District)
admin.site.register(division)
admin.site.register(Blood)


