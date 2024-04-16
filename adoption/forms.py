from django import forms


class InterestForm(forms.Form):
    email = forms.EmailField(
        label="Enter your email to express interest", required=True
    )
    message = forms.CharField(
        widget=forms.Textarea, required=False, label="Add a message (optional)"
    )
