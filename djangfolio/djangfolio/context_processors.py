from django.conf import settings
from profiles.models import Profile, Career, Project


def google_analytics(request):
    """
    Context processor for google analytics key.

    :param request: the request
    :return: the google analytics key if it is defined
    """
    try:
        return {"GOOGLE_ANALYTICS_KEY": settings.GOOGLE_ANALYTICS_KEY}
    except AttributeError:
        return {}


def active_user(request):
    """
    Get the active user.

    :param request: the request
    :return: the active user if defined
    """
    try:
        active_profile = Profile.objects.get(active=True)
        active_profile.career = Career.objects.filter(profile=active_profile)
        active_profile.projects = Project.objects.filter(profile=active_profile)
        return {"active_user": active_profile}
    except Profile.DoesNotExist:
        return {}
