from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Sponsor)
admin.site.register(Student)
admin.site.register(StudentSponsor)
admin.site.register(University)


