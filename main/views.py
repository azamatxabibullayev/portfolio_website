from django.shortcuts import render
from .models import Project, Link, Resume, Skill, About


def landing_page(request):
    projects = Project.objects.all()
    links = Link.objects.all()
    resume = Resume.objects.last()
    skills = Skill.objects.all()
    about = About.objects.last()

    context = {
        'projects': projects,
        'links': links,
        'resume': resume,
        'skills': skills,
        'about': about,
    }
    return render(request, 'landing_page.html', context)
