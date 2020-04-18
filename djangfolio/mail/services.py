from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from smtplib import SMTPException
from profiles.models import Profile


def generate_contact_email(request, name, title, message, email_address):
    """
    Generate a contact email.

    :param request: the request
    :param name: the name the user entered in the contact form
    :param title: the title the user entered in the contact form
    :param message: the message the user entered in the contact form
    :param email_address: the email address the user entered in the contact form
    :return: a rendered text_content and html_content in the following format: text_content, html_content
    """
    template = get_template("mail/email/contact_mail.html")
    template_text = get_template("mail/email/contact_mail.txt")

    active_profile = Profile.objects.get(active=True)

    context = {
        "name": name,
        "title": title,
        "message": message,
        "email": email_address,
        "url": request.META["HTTP_HOST"],
        "admin_first_name": active_profile.first_name,
    }

    text_content = template_text.render(context)
    html_content = template.render(context)

    return text_content, html_content


def send_email(request, text_content, html_content, email_address):
    """
    Send an email.

    :param request: the request
    :param text_content: the text_content
    :param html_content: the html_content
    :param email_address: the email address to send to
    :return: True if the mail was send successfully, False otherwise
    """
    msg = EmailMultiAlternatives(
        "{}: contact form".format(request.META["HTTP_HOST"]),
        text_content,
        settings.EMAIL_HOST_USER,
        [email_address],
    )
    msg.attach_alternative(html_content, "text/html")
    try:
        msg.send()
    except SMTPException:
        return False

    return True
