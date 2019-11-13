from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):              #отображение модели в админке
    post_display = ('title', 'slug', 'publish')
    list_filter = ('publish',)
    search_field = ('title', 'body')
    prepopulated_fields = {'slug' : ('title',)}
    date_hierarchy = 'publish'
    ordering = ['publish']


admin.site.register(Post, PostAdmin)               #добавляем модель Пост в Админку сайта, для управления постами
