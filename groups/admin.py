from django.contrib import admin
from .models import *

class GroupMemberInLine(admin.TabularInline):
    model = GroupMember

admin.site.register(Group)
