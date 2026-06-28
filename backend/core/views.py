from django.shortcuts import render
from .models import Profile
from skills.models import Skill

def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()

    context = {
        "profile": profile,
        "skills": skills,
    }

    return render(request, "home.html", context)