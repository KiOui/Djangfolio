from django.views.generic import TemplateView
from django.shortcuts import render
from mail.services import send_email, generate_contact_email
from .services import get_contact_form


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
        context = {"contact_form": get_contact_form()}
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        """
        POST request function for the home view.

        :param request: the request
        :param kwargs: keyword arguments
        :return: a render of the index.html page, either with a succeeded or failed message indicating if the request
        was send successfully or not
        """
        form = get_contact_form(request.POST)
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
                context["contact_form"] = get_contact_form()
                return render(request, self.template_name, context)
            else:
                context["failed"] = True
                return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)
