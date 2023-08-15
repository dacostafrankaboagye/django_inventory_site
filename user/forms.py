

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#import the profile

from .models import Profile

class CreateUserForm(UserCreationForm):
	email = forms.EmailField()

	#defining how the forms look like
	class Meta:
		#which model do we want to create the forms for - User of course
		model = User
		# you can put in a list or tuple for the fields
		
		#fields = '__all__'  #shows all the fields
		fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

	# what are the kinds of things we need
	class Meta:
		model = User
		fields = ['username', 'email']



#we also what to update the profile
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['address', 'phone', 'image']

