from django.contrib import admin
from .models import Place, Image
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableStackedInline


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ['file', 'get_preview']
    extra = 0

    def get_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 200px; max-width: 800px;" />',
            obj.file.url,
            )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline
    ]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
