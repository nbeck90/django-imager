from django.contrib import admin
from imagerprofile.models import ImagerProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class ImagerUserInline(admin.StackedInline):
    model = ImagerProfile
    can_delete = False
    verbose_name_plural = 'imager user'
    extra = 0


class UserAdmin(UserAdmin):
    inlines = (ImagerUserInline, )
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')

    def get_inline_instances(self, request, obj=None):
        if obj is None:
            return []
        else:
            return [inline(self.model, self.admin_site)
                    for inline in self.inlines]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
