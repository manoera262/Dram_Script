from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from core.forms import SignUpForm, ContactUsForm, UploadScriptForm


@login_required
def home(request):
    # messages.add_message(request, constants.SUCCESS, message="Details Saved Welcome %s %s" % (request.user, request) )
    user1 = get_object_or_404(User, username=request.user)
    return render(request, 'dashboard.html', {'user': user1})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user_type = form.cleaned_data['user_type']
            # referral_id = form.cleaned_data['referral_id']
            # UserProfile(user_type=user_type, referral_id=referral_id, user=user).save()
            # print(form.cleaned_data['user_type'], form.cleaned_data['referral_id'], form.cleaned_data['username'])
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.add_message(request, constants.SUCCESS, message="Details Saved Welcome %s" % request.user, )
            return redirect('home')  # todo change it
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user_type = form.cleaned_data['user_type']
            # referral_id = form.cleaned_data['referral_id']
            # UserProfile(user_type=user_type, referral_id=referral_id, user=user).save()
            # print(form.cleaned_data['user_type'], form.cleaned_data['referral_id'], form.cleaned_data['username'])
            user.save()
            messages.add_message(request, constants.SUCCESS, message="Your request has been registered, We will get back to you soon", )
            return redirect('home')  # todo change it
    else:
        form = ContactUsForm()
    return render(request, 'contact-us.html', {'form': form})


@login_required
def upload_script(request):
    if request.method == 'POST':
        form = UploadScriptForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_by = request.user
            user.script_file = form.cleaned_data['script_file']
            user.save()
            messages.add_message(request, constants.SUCCESS, message="Script Uploaded", )
            return redirect('home')  # todo change it
    else:
        form = UploadScriptForm()
    return render(request, 'ScriptUpload.html', {'form': form})