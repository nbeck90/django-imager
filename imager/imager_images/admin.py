from django.contrib import admin
from imager_images.models import ImagerAlbum, ImagerPhoto
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class ImagerUserInline(admin.StackedInline):
    model = ImagerAlbum, ImagerPhoto
    can_delete = False
    verbose_name_plural = 'imager albums'


class UserAdmin(UserAdmin):
    inlines = (ImagerUserInline, )


admin.site.register(ImagerAlbum)
admin.site.register(ImagerPhoto)
