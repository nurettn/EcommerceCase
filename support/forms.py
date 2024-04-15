from django import forms
from django.core.validators import RegexValidator

from .models import StoreInformation, UserInformation

phone_regex = RegexValidator(
    regex=r"^05\d{9}$",
    message="Phone number must be entered in the format: '05xxxxxxxxx'.",
)


class UserInformationForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = ["first_name", "last_name", "email", "phone_number"]

    def __init__(self, *args, **kwargs):
        super(UserInformationForm, self).__init__(*args, **kwargs)
        self.fields["phone_number"].validators.append(phone_regex)


class StoreInformationForm(forms.ModelForm):
    class Meta:
        model = StoreInformation
        fields = ["store_url", "platform"]
