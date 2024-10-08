from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required 
from .models import Study
from .forms import StudyForm, UserForm

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Study.objects.create(user=user) 
            auth_login(request, user)  
            return redirect('login')  
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('main_view') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login') 

def main_view(request):
    studies = Study.objects.filter(user=request.user)
    return render(request, 'study_list.html', {'studies': studies})

@login_required
def add_study(request):    
    if request.method == 'POST':
        form =StudyForm(request.POST)
        if form.is_valid():
                study = form.save(commit=False)
                study.user = request.user 
                study.save()
                return redirect('main_view')
    else:
        form = StudyForm()
    return render(request, 'add_study.html', {'form': form})

@login_required
def view_study(request, pk):
    study = get_object_or_404(Study, pk=pk, user=request.user)  
    return render(request, 'view_study.html', {'study': study})

@login_required
def edit_study(request, pk):
    study = get_object_or_404(Study, pk=pk, user=request.user)  
    if request.method == 'POST':
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            form.save()
            return redirect('main_view')  
    else:
        form = StudyForm(instance=study)
    return render(request, 'edit_study.html', {'form': form, 'study': study})

@login_required
def delete_study(request, pk):
    study = get_object_or_404(Study, pk=pk, user=request.user)  
    if request.method == 'POST':
        study.delete()
        return redirect('main_view')  
    return render(request, 'delete_study.html', {'study': study})  
