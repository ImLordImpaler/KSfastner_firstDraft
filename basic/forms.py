from django.forms import ModelForm
from .models import CallBack

class CallBackForm(ModelForm):
    class Meta:
        model = CallBack
        exclude = []