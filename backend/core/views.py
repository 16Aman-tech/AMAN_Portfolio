from django.shortcuts import render
from .models import Profile, Experience
from skills.models import Skill
from projects.models import Project
from certificates.models import Certificate

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences=Experience.objects.all()
    certificates = Certificate.objects.all()

    context = {
        "profile": profile,
        "skills": skills,
        "projects": projects,
        "certificates": certificates,
        "experiences":experiences
    }

    return render(request, "home.html", context)