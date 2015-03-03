from django.contrib import admin
from ImagerProfile.models import ImagerProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# admin.site.unregister(User)


class ImagerUserInline(admin.StackedInline):
    model = ImagerProfile
    can_delete = False
    verbose_name_plural = 'imager user'


class UserAdmin(UserAdmin):
    inlines = (ImagerUserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
