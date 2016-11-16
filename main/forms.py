from django import forms

class SurveyForm(forms.Form):
    human = forms.BooleanField(label="Are you human?",required=False)
    age = forms.IntegerField(label="How old are you?")
    color  = forms.ChoiceField(
        label="What color is your eye?",
        choices=(('bl','Blue'),('br','Brown'),('bl','Black'),('gr','Green'),('rd','Red')),)
    name = forms.CharField(label="What's your name?",)
    subscription = forms.BooleanField(label="Do you want to subscribe?",required=False)
    email = forms.EmailField(label="Your email:",)

    def clean(self):
        cleaned_data = super(SurveyForm,self).clean()
        if cleaned_data['human'] is False and cleaned_data['color'] == 'rd':
            raise forms.ValidationError("Humans cannot have red eyes!")
        return cleaned_data