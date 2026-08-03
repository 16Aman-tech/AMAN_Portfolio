from django.http import Http404, FileResponse
from core.models import Profile
from .models import ResumeDownload


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    return ip


def download_resume(request):

    profile = Profile.objects.first()

    if not profile or not profile.resume:
        raise Http404("Resume not found.")

    ResumeDownload.objects.create(
        ip_address=get_client_ip(request)
    )

    response = FileResponse(
        profile.resume.open("rb"),
        as_attachment=True
    )

    return response