from django.shortcuts import render, redirect
from .models import Profile, Experience

from skills.models import Skill
from projects.models import Project
from certificates.models import Certificate
from education.models import Education
from coding.models import CodingProfile
from contact.models import Contact
from contact_messages.models import ContactMessage
from analytics.models import Visitor, ResumeDownload

from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


def home(request):

    # ==========================
    # CONTACT FORM
    # ==========================
    if request.method == "POST":

        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

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

        return redirect("home")

    # ==========================
    # VISITOR TRACKING
    # ==========================

    ip = request.META.get("REMOTE_ADDR")

    if not Visitor.objects.filter(ip_address=ip).exists():
        Visitor.objects.create(ip_address=ip)

    # ==========================
    # FETCH DATA
    # ==========================

    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    certificates = Certificate.objects.all()
    education = Education.objects.all()
    coding_profiles = CodingProfile.objects.all()
    contact = Contact.objects.first()

    # ==========================
    # ANALYTICS COUNTS
    # ==========================

    visitor_count = Visitor.objects.count()
    message_count = ContactMessage.objects.count()
    project_count = Project.objects.count()
    certificate_count = Certificate.objects.count()
    download_count = ResumeDownload.objects.count()

    context = {

        "profile": profile,
        "skills": skills,
        "projects": projects,
        "experiences": experiences,
        "certificates": certificates,
        "education": education,
        "coding_profiles": coding_profiles,
        "contact": contact,

        # Analytics
        "visitor_count": visitor_count,
        "message_count": message_count,
        "project_count": project_count,
        "certificate_count": certificate_count,
        "download_count": download_count,

    }

    return render(request, "home.html", context)