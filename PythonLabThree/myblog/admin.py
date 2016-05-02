from django.contrib import admin
from myblog.models import Post

# slug field that automatically filled in the admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'title')
    search_fields = ['title']

    class Meta:
        model = Post

# BlogPost model is registered
admin.site.register(Post, PostAdmin)