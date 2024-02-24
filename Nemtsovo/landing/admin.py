from .models import *
from django.contrib.contenttypes.admin import GenericTabularInline, GenericStackedInline
import admin_thumbnails
from django.forms import TextInput, Select
from django.db.models import F, Max


class AdminModelWithOrder(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if not hasattr(self.model, 'order'):
            return form

        current_max_order = 0
        if self.model.objects.exists():
            current_max_order = self.model.objects.aggregate(Max("order"))['order__max']

        if obj and obj.pk:
            form.base_fields['order'].widget = Select(choices=[(x, x) for x in range(1, current_max_order + 1)])
        else:
            form.base_fields['order'].widget = Select(choices=[(x, x) for x in range(1, current_max_order + 2)])
            form.base_fields['order'].initial = current_max_order + 1

        return form

    def save_model(self, request, obj, form, change):
        if hasattr(self.model, 'order'):
            self.model.objects.filter(order__gte=obj.order).update(order=F("order") + 1)
        return super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        if hasattr(self.model, 'order'):
            self.model.objects.filter(order__gt=obj.order).update(order=F("order") - 1)
        return super().delete_model(request, obj)


@admin_thumbnails.thumbnail('miniature', 'Миниатюра')
@admin_thumbnails.thumbnail('file', 'Фото/Видео')
class AttachmentInline(GenericTabularInline):
    model = Attachment
    extra = 5


@admin.register(House)
class HouseAdmin(AdminModelWithOrder):
    list_display = ("name", "start_price")
    inlines = [AttachmentInline]
    list_filter = ("start_price",)
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
class WellnessTreatmentAdmin(AdminModelWithOrder):
    list_display = ("name", "start_price")
    inlines = [AttachmentInline]
    list_filter = ("start_price",)
    search_fields = ("name", "description", "start_price")
    save_on_top = True


@admin.register(Action)
class ActionAdmin(AdminModelWithOrder):
    list_display = ("name", 'get_price_or_display_free')
    inlines = [AttachmentInline]
    list_filter = ("start_price",)
    search_fields = ("name", "description", "start_price")
    save_on_top = True

    @admin.display(description='Начальная цена')
    def get_price_or_display_free(self, obj):
        return obj.start_price if obj.start_price > 0 else "Бесплатно"


@admin.register(OurProduct)
class OurProductAdmin(AdminModelWithOrder):
    list_display = ("name", "price", "is_available")
    inlines = [AttachmentInline]
    list_filter = ("is_available", 'price')
    search_fields = ('name', 'description', 'price')
    save_on_top = True
    list_editable = ('is_available',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", 'is_passed')
    inlines = [AttachmentInline]
    list_filter = ["date"]
    ordering = ['-date']
    save_on_top = True
    search_fields = ("title", "description")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    inlines = [AttachmentInline]
    list_filter = ["date"]
    ordering = ['-date']
    save_on_top = True
    search_fields = ("title", "description")


admin.site.register(Period)
# admin.site.register(House, HouseAdmin)
# admin.site.register(BookingConditions, BookingConditionsAdmin)
