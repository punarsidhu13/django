from django.contrib import admin
from myapp.models import Blog
from datetime import timedelta
from django.utils import timezone

# Register your models here.



class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'description', 'published_on']
    list_filter= ['is_published']
    search_fields = ['title']

    def is_recently_published(self,obj):
        if obj.is_published == True:
            var = obj.published_on
            now_time = timezone.now()

             #tommorow 
            blog_end_time = now_time + timezone.timedelta(days=2)

            #yesterday
            blog_start_time = now_time - timezone.timedelta(days=2) 

            if  var > blog_start_time and var < blog_end_time:
                return True
            else:
                return False
        pass

admin.site.register(Blog, BlogAdmin)    