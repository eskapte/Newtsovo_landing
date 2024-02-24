from .models import *
from django.contrib.contenttypes.admin import GenericTabularInline
import admin_thumbnails
from django.forms import TextInput
from adminsortable2.admin import SortableAdminBase, SortableGenericInlineAdminMixin, SortableAdminMixin


@admin_thumbnails.thumbnail('miniature', 'Миниатюра')
@admin_thumbnails.thumbnail('file', 'Фото/Видео')
class AttachmentInline(SortableGenericInlineAdminMixin, GenericTabularInline):
    model = Attachment
    extra = 5


@admin.register(House)
class HouseAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("name", "start_price", 'order')
    inlines = [AttachmentInline]
    search_fields = ("name", "description", "start_price")
    save_on_top = True


class AdditionalInfoItemInline(admin.StackedInline):
    model = AdditionalInfoItem
    extra = 5
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': 200})}
    }


@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ("inner_name", "displayed_name")
    search_fields = ("inner_name", 'displayed_name')
    inlines = [AdditionalInfoItemInline]
    save_on_top = True


@admin.register(WellnessTreatment)
class WellnessTreatmentAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("name", "start_price", 'order')
    inlines = [AttachmentInline]
    search_fields = ("name", "description", "start_price")
    save_on_top = True


@admin.register(Action)
class ActionAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ("name", 'get_price_or_display_free', 'order')
    inlines = [AttachmentInline]
    search_fields = ("name", "description", "start_price")
    save_on_top = True

    @admin.display(description='Начальная цена')
    def get_price_or_display_free(self, obj):
        return obj.start_price if obj.start_price > 0 else "Бесплатно"


@admin.register(OurProduct)
class OurProductAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ("name", "price", "is_available")
    inlines = [AttachmentInline]
    list_filter = ("is_available",)
    search_fields = ('name', 'description', 'price')
    save_on_top = True
    list_editable = ('is_available',)


@admin.register(Event)
class EventAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ("title", "date", 'is_passed')
    inlines = [AttachmentInline]
    list_filter = ["date"]
    ordering = ['-date']
    save_on_top = True
    search_fields = ("title", "description")


@admin.register(News)
class NewsAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ("title", "date")
    inlines = [AttachmentInline]
    list_filter = ["date"]
    ordering = ['-date']
    save_on_top = True
    search_fields = ("title", "description")


admin.site.register(Period)
# admin.site.register(House, HouseAdmin)
# admin.site.register(BookingConditions, BookingConditionsAdmin)
