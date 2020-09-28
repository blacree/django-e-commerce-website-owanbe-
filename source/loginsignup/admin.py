from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import LoginInformation, Account, loginhistory

# Register your models here.
admin.site.register(LoginInformation)


class  AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter= ()
    fieldsets = ()

class HistoryLogin(admin.ModelAdmin):
    list_display = ['__str__', 'Timeloggedin']
    class Meta:
        model = loginhistory

admin.site.register(loginhistory, HistoryLogin)

admin.site.register(Account, AccountAdmin)
