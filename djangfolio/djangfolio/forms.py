from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class ContactFormCaptcha(forms.Form):
    """Recaptcha contact form."""

    name = forms.CharField(label="Name")
    title = forms.CharField(label="Title")
    email = forms.EmailField(label="Email-address")
    content = forms.CharField(
        widget=forms.TextInput(attrs={"id": "contact_content"}),
        label="Message",
        required=False,
    )
    captcha = ReCaptchaField(widget=ReCaptchaV3(api_params={"hl": "nl"}), label="")
