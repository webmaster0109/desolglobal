from django.contrib import admin
from django.http import HttpResponseRedirect
from desol_home.models.global_links import *
from desol_home.models.reviews import CustomerReview
from desol_home.models.faqs import FaqSection
from desol_home.models.blogs import BlogsDetail
from desol_home.models.customer_leads import CustomersDetails
from django.contrib import messages
from adminsortable2.admin import SortableAdminMixin
from unfold.admin import ModelAdmin
from django.contrib.auth.models import Group, User
from import_export.admin import ImportExportModelAdmin
from import_export import resources

admin.site.unregister((Group, User))


@admin.register(Logo)
class LogoAdmin(ModelAdmin):
    pass

@admin.register(SocialMediaLinks)
class SocialMediaLinksAdmin(ModelAdmin):
    pass

@admin.register(Favicon)
class FaviconAdmin(ModelAdmin):
    pass

@admin.register(CustomerReview)
class CustomerReviewAdmin(ModelAdmin):
    pass

@admin.register(FaqSection)
class FaqSectionAdmin(ModelAdmin):
    pass

@admin.register(GoogleMapEmbed)
class GoogleMapEmbedAdmin(ModelAdmin):
    pass

class CustomersDetailsResource(resources.ModelResource):
    class Meta:
        model = CustomersDetails
        fields = ('customer_id', 'first_name', 'last_name', 'email', 'phone', 'country', 'position', 'destination', 'created_at')
        export_order = fields

@admin.register(CustomersDetails)
class CustomersDetailsAdmin(ModelAdmin, ImportExportModelAdmin):
    resource_class = CustomersDetailsResource
    list_display = ['first_name', 'last_name', 'email', 'phone', 'country', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'country', 'position', 'destination']
    list_filter = ['created_at', 'destination', 'country']

@admin.register(BlogsDetail)
class BlogsDetailAdmin(ModelAdmin):
    list_display = ['title', 'slug', 'created_at', 'updated_at']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

    def copy_objects(self, request, queryset):
        for obj in queryset:
            obj.id = None
            obj.title = f"{obj.title} Copy"
            obj.slug = f"{obj.slug}-copy"
            obj.save()

    copy_objects.short_description = "Copy Selected Blog Detail"

    # Register the custom action with the ModelAdmin class
    actions = ['copy_objects']