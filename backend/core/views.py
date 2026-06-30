from django.shortcuts import render, redirect
from .models import Profile, Experience
from skills.models import Skill
from projects.models import Project
from certificates.models import Certificate
from education.models import Education
from coding.models import CodingProfile
from contact.models import Contact
from contact_messages.models import ContactMessage

from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def home(request):

    if request.method == "POST":

        print(request.POST)

        # Save message in database
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

        # Send email notification
        send_mail(
            subject=f"📩 New Portfolio Contact: {request.POST.get('subject')}",
            message=f"""
New message received from your portfolio.

Name: {request.POST.get('name')}

Email: {request.POST.get('email')}

Subject: {request.POST.get('subject')}

Message:

{request.POST.get('message')}
""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        messages.success(
            request,
            "Your message has been sent successfully!"
        )

        print("MESSAGE SAVED")

        return redirect("home")

    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    certificates = Certificate.objects.all()
    education = Education.objects.all()
    coding_profiles = CodingProfile.objects.all()
    contact = Contact.objects.first()

    context = {
        "profile": profile,
        "skills": skills,
        "projects": projects,
        "experiences": experiences,
        "certificates": certificates,
        "education": education,
        "coding_profiles": coding_profiles,
        "contact": contact,
    }

    return render(request, "home.html", context)