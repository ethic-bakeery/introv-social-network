from django.contrib import admin
from .models import *

admin.site.register(Page)
admin.site.register(Post)
admin.site.register(Room)
admin.site.register(User)
# admin.site.register(Admin)
admin.site.register(RoomMembership)
admin.site.register(PageFollow)
admin.site.register(Message)
