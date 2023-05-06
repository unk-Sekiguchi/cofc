from django import forms

class ChatForm(forms.Form):
    age_sentence = forms.IntegerField(label='年齢', required=True)
    GENDER = (("女性","女性"),("男性","男性"))
    gender_sentence = forms.ChoiceField(label='性別', widget=forms.Select,choices=GENDER, required=True)
    jobs_sentence = forms.CharField(label='職業', required=True)
    other_sentence = forms.CharField(label='その他の要素', required=True)