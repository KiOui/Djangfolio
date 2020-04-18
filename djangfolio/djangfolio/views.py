from django.views.generic import TemplateView
from .forms import ContactFormCaptcha
from django.conf import settings
from django.shortcuts import render
from mail.services import send_email, generate_contact_email


class IndexView(TemplateView):
    """Home view."""

    template_name = "djangfolio/index.html"

    def get(self, request, **kwargs):
        """
        GET request function for home view.

        :param request: the request
        :param kwargs: keyword arguments
        :return: a render of the index.html page, either with or without a contact form (if email settings are
        specified)
        """
        if settings.EMAIL_HOST and settings.EMAIL_PORT:
            return render(
                request, self.template_name, {"contact_form": ContactFormCaptcha()}
            )
        else:
            return render(request, self.template_name, {})

    def post(self, request, **kwargs):
        """
        POST request function for the home view.

        :param request: the request
        :param kwargs: keyword arguments
        :return: a render of the index.html page, either with a succeeded or failed message indicating if the request
        was send successfully or not
        """
        if settings.EMAIL_HOST and settings.EMAIL_PORT:
            form = ContactFormCaptcha(request.POST)
        else:
            return render(request, self.template_name, {})

        context = {"contact_form": form}

        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            title = form.cleaned_data.get("title")
            message = form.cleaned_data.get("content")
            text_content, html_content = generate_contact_email(
                request, name, title, message, email
            )
            if send_email(request, text_content, html_content, email):
                context["succeeded"] = True
                context["contact_form"] = ContactFormCaptcha()
                return render(request, self.template_name, context)
            else:
                context["failed"] = True
                return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)
