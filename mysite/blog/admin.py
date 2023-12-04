from django.contrib import admin
from . models import Posts, Category, Comments


class CommentsItemInline(admin.TabularInline):
    model = Comments
    raw_id_fields = ['post']


class PostsAdmin(admin.ModelAdmin):
    search_fields = ['title','intro','content']
    list_display = ['title','slug', 'category', 'date_posted', 'status']
    list_filter = ['category','date_posted','status']
    inlines = [CommentsItemInline]
    prepopulated_fields = {'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug':('title',)}

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name','post','date_posted']



admin.site.register(Posts,PostsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comments, CommentsAdmin)
# Register your models here.
