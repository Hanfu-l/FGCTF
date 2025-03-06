from django.contrib import admin


from .models import Topic,UserDockerData,Score
# Register your models here.
admin.site.register(Topic)
admin.site.register(UserDockerData)
admin.site.register(Score)