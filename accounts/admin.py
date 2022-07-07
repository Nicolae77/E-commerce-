from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login' , 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

# class UserProfileAdmin(admin.ModelAdmin):
#     def thumbmail(self, object):
#         return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.profile_picture.url))
#     thumbmail.short_description = 'Profile Picture'
#     list_display = ('thumbmail', 'user', 'city', 'state', 'country')

admin.site.register(Account, AccountAdmin)
# admin.site.register(UserProfile, UserProfileAdmin)
