from django.contrib import admin
from imager_images.models import ImagerAlbum, ImagerPhoto
# from django.contrib.auth.admin import UserAdmin


class PhotoAdmin(admin.ModelAdmin):
    model = ImagerPhoto
    list_display = ('picture', 'title', 'user',
                    'description', 'date_modified')
    list_filter = ['albums', 'user']
    search_fields = ['title', 'albums', 'user']
    readonly_fields = ('date_uploaded', 'date_modified')


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'description',
                    'date_created', 'date_modified')
    list_filter = ['published', 'user']
    search_fields = ['title', 'published', 'user']
    readonly_fields = ('date_modified', 'date_created')


admin.site.register(ImagerAlbum, AlbumAdmin)
admin.site.register(ImagerPhoto, PhotoAdmin)
