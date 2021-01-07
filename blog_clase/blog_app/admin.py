from django.contrib import admin

# Register your models here.


from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
 list_display = ('titulo', 'slug', 'autor', 'publicado', 'estado')
 search_fields = ('titulo', 'body')
 list_filter = ('estado', 'creado', 'publicado', 'autor')
 prepopulated_fields = {'slug': ('titulo',)}
 raw_id_fields = ('autor',)
 date_hierarchy = 'publicado'
 ordering = ('estado', 'publicado')


 # EDICIÓN QUE SE PUEDE AÑADIR AL ADMINISTRADOR:
 # list_filter = ('status', 'created', 'publish', 'author')
 # prepopulated_fields = {'slug': ('title',)}
 # raw_id_fields = ('author',)
 # date_hierarchy = 'publish'
 # ordering = ('status', 'publish')