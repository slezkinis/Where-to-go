from django.contrib import admin
from .models import Place, Image
from django.utils.safestring import mark_safe


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['get_preview']
    fields = ['title', 'file', 'get_preview']
    def get_preview(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.file.url,
            width=obj.file.width / 3,
            height=obj.file.height / 3,
            )
    )

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline
    ]


admin.site.register(Image)