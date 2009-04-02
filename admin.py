from django.contrib import admin
from models import Impersonation

class ImpersonationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Impersonation, ImpersonationAdmin)
