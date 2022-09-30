from django.contrib import admin
from .models import comments,registration,slot_details,user_with_slotdetail



# Register your models here.

admin.site.register(comments)
admin.site.register(registration)
admin.site.register(slot_details)
admin.site.register(user_with_slotdetail)