from django.contrib import admin
from .models import UserWithPhone, Course, Request

admin.site.register(UserWithPhone)
admin.site.register(Course)
admin.site.register(Request)