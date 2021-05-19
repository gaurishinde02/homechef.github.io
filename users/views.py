from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# django takes care of form creation and validation, generating HTML forms, etc. through UserCreation class
# Only the submit button is not included in this form, hence it need to be added explicitly in the HTML page
# We pass the 'form' dictionary to the render function
# ---------------------------------------------------------------
# Messages are something that can be shown for an instant on the UI for the user
# Different types of messages:
# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
# -------------------------------------------------------------
# We wanted to add more fields to Djano's UserCreationForm.
# So we created a forms.py in the users app, created a class in it,
# named UserRegisterForm and used it the users views.py
# Hence, the UserCreationForm import is no longer needed in the views.py


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('home-page')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
