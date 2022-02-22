from django.contrib import admin
from work_record.models import PolicyDocumentModel, IndustryDevelopmentModel


@admin.register(PolicyDocumentModel)
class PolicyDocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publish_time', 'is_alter', 'link']


@admin.register(IndustryDevelopmentModel)
class IndustryDevelopmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'industry_category', 'file_link', 'publish_time']
