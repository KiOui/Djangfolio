from .forms import ContactForm, ContactFormCaptcha
from django.conf import settings


def get_contact_form(post_data=None):
    """
    Get a contact form.

    :param post_data: the post data to put in the contact form.
    :return: a ContactFormCaptcha if Captcha settings are specified, a ContactForm otherwise
    """
    if settings.RECAPTCHA_PUBLIC_KEY and settings.RECAPTCHA_PRIVATE_KEY:
        return ContactFormCaptcha(post_data)
    else:
        return ContactForm(post_data)
