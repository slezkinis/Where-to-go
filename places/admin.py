from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminBase, SortableStackedInline


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ['file', 'get_preview']
    extra = 0

    def get_preview(self, obj):
        return mark_safe('<img src="{url}" height=300 />'.format(
            url = obj.file.url,
            )
    )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
