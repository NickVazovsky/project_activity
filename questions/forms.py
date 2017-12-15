from django import forms

from questions.models import SaveUrl


class PostForm(forms.ModelForm):

    class Meta:
        model = SaveUrl
        exclude = ["url"]
