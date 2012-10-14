from django import forms
from scenes.models import Scene, Entity, FreeTextQuestion

class FreeTextQuestionForm(forms.ModelForm):
    scene = forms.ModelChoiceField(queryset=Scene.objects.all(),
                                   widget=forms.HiddenInput())
    entity = forms.ModelChoiceField(queryset=Entity.objects.all(),
                                    widget=forms.HiddenInput())

    class Meta:
        model = FreeTextQuestion

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question', None)
        super(FreeTextQuestionForm, self).__init__(*args, **kwargs)
        if question:
            self.fields['answer'].label = question
