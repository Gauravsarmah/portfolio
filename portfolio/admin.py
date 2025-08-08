from django.contrib import admin

# Register your models here.
from .models import Skill, Project , BlogPost , skill_header

admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(BlogPost)
admin.site.register(skill_header)