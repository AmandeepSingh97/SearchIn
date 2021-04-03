from django.contrib import admin
from friends.models import friendrequest,friendlist
# Register your models here.

class friendlistadmin(admin.ModelAdmin):
    list_filter = ['user']
    list_display = ['user']
    search_field = ['user']
    
    class meta:
        model = friendlist

admin.site.register(Friendlist,friendlistadmin)


class friendrequestadmin(admin.ModelAdmin):
    list_filter = ['sender','receiver']
    list_display = ['sender','receiver']
    list_fields = ['sender__username','sender__email''receiver__username','receiver__email']

    class Meta:
        model = friendrequest

admin.site.register(friendrequest,friendrequestAdmin)
