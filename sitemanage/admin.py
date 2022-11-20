from django.contrib import admin
from .models import SiteConfig
from django.contrib.sites.models import Site

# 管理画面の表示内容を定義するファイル
@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'meta_title',)
    list_display_links = ('meta_title',)

