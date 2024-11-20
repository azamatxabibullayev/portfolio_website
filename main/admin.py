from django.contrib import admin
from .models import Project, Link, Resume, Skill, About


admin.site.register(Project)
admin.site.register(Link)
admin.site.register(Resume)
admin.site.register(Skill)
admin.site.register(About)
