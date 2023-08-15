from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm

#adding flash messages
from django.contrib import messages

# Create your views here.

def register(request):
	if request.method == 'POST':
		# pass the info
		#form = UserCreationForm(request.POST)
		  # instead of the UserCreationForm, we use the one when have customised ie CreateUserForm
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user_name = form.cleaned_data.get('username') #we are grabbing the name. You can check the other fields we specified in the forms.py
			messages.success(request, f'{user_name} has been created. Continue to LOG IN')
			#return redirect('dashboard-index')
			return redirect('user-login')
	else:
		# just leave it like that as I created it
		#form = UserCreationForm()
		form = CreateUserForm()
	context = {
		'form': form
	}
	return render(request, 'user/register.html', context)


def profile(request):
	return render(request, 'user/profile.html')


def profile_update(request):
	if request.method == 'POST':
		user_form =  UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('user-profile')
	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.profile)

	context = {
		'user_form': user_form,
		'profile_form': profile_form

	}
	return render(request, 'user/profile_update.html', context)