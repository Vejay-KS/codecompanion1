from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CodeCompanionUser


# Create your forms here.

class NewUserForm(UserCreationForm):
	choices = CodeCompanionUser.UserRoles.choices
	email = forms.EmailField(required=True)
	ROLE = forms.ChoiceField(choices=choices)

	class Meta:
		model = CodeCompanionUser
		fields = ("username", "password1", "password2", "email")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.ROLE = self.cleaned_data['ROLE']
		if commit:
			user.save()
		return user