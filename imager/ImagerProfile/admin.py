from django.contrib import admin
from imagerprofile.models import ImagerProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# admin.site.unregister(User)


class ImagerUserInline(admin.StackedInline):
    model = ImagerProfile
    can_delete = False
    verbose_name_plural = 'imager user'
    extra = 0


class UserAdmin(UserAdmin):
    inlines = (ImagerUserInline, )

    # def get_inline_formsets(self, request, formsets, inline_instances,
    #                         obj=None):
    #     if obj is None:
    #         inline_instances.remove(ImagerUserInline)
    #     else:
    #         inline_instances.add(ImagerUserInline)
    #     super(UserAdmin, self).get_inline_formsets(request, formsets,
    #                                                inline_instances, obj)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
