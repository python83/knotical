from django.contrib import admin
from taskmanager.models import KnotsTopics, KnotsCategory, KnotsStatus, KnotsUrgency, Knots
# Register your models here.

admin.site.register(KnotsTopics)
admin.site.register(KnotsCategory)
admin.site.register(KnotsStatus)
admin.site.register(KnotsUrgency)
admin.site.register(Knots)
