from django import forms
from cofc_app.models import CharacterInput

class ChatForm(forms.ModelForm):
    class Meta:
        model = CharacterInput
        fields = ('age','gender','job','others')
    """
        age_sentence = forms.IntegerField(label='年齢', required=True)
        GENDER = (("女性","女性"),("男性","男性"))
        gender_sentence = forms.ChoiceField(label='性別', widget=forms.Select,choices=GENDER, required=True)
        jobs_sentence = forms.CharField(label='職業', required=True)
        other_sentence = forms.CharField(label='その他の要素', widget=forms.Textarea)
    """