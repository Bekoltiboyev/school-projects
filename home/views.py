from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile, ProjectModel
from hitcount.utils import get_hitcount_model
from hitcount.views import HitCountMixin

def home(request):
    online_users = Profile.objects.filter(is_online=True).count()
    
    ctx = {
        "online_users": online_users
    }
    return render(request, 'index.html', ctx)



def ProjectPageView(request):
    project_page = ProjectModel.objects.all()
    
    
    ctx = {
        "project_page": project_page, 
    }
    return render(request, 'project_page.html',ctx)

def UserLogin(request):
    form = LoginForm()
    ctx = {
        "form": form,
    }
    if request.POST:
        userName = request.POST['UserName']
        password = request.POST['password']
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Xush kelibsiz!")
            return redirect('home')
        else:
            messages.error(request, "username yoki parol xato qayta urnib koring!")
            return redirect('login')
    else:
        return render(request, 'login.html', ctx)

def userLogout(request):
    logout(request)
    return redirect('login')


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')
        else:
            messages.error(request, "kuchliroq parol kiriting!")
            return redirect('signup')
    ctx = {
        "form": form
    }
    
    return render(request, 'signup.html', ctx)

@login_required
def sectionView(request):
    return render(request, 'section.html',)


@login_required
def ProfileView(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            tel_nomer = form.cleaned_data['tel_nomer']
            profile_data = Profile(name=name, email=email, tel_nomer=tel_nomer)
            profile_data.save()
            return redirect('/')
        else:
            print("error")
            return redirect('profile')
    data = request.user.profile
    ctx = {
        "data": data,
        "form": form
    }
    return render(request, 'profile.html', ctx)


@login_required
def EditProfileView(request, id_user):
    data = Profile.objects.get(id=id_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return redirect('edit_profile')
    form = ProfileForm(instance=data)
    ctx = {
        "form": form,
        "data": data,
        "id_user": id_user
    }
    return render(request, 'edit.html', ctx)


@login_required
def ProjectView(request, pcjt_id):
    profile_id = Profile.objects.get(id=pcjt_id)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=profile_id)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            project_image = form.cleaned_data['project_image']
            github_link = form.cleaned_data['github_link']
            yonalish = form.cleaned_data['yonalish']
            profile_data = ProjectModel(name=name, price=price, project_image=project_image, profiles=profile_id, github_link=github_link, yonalish=yonalish  )
            profile_data.save()
        else:
            print('error')
    
    form = ProjectForm()
    projects = ProjectModel.objects.filter(profiles_id=profile_id)

    ctx = {
        "form": form,
        "projects": projects,
        
    }
    return render(request, 'project.html', ctx)


@login_required
def EditProjectView(request, edit_id):
    project_edit = ProjectModel.objects.get(id=edit_id)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project_edit)
        if form.is_valid():
            form.save()
            return redirect("project")
        else:
            print("error")
    form = ProjectForm(instance=project_edit)
    ctx = {
        "form": form,
        "project_edit": project_edit
    }
    return render(request, 'edit_p.html', ctx)


@login_required
def DeleteProjectView(request, delete_id):
    project_delete = ProjectModel.objects.get(id=delete_id)
    if request.POST:
        project_delete.delete()
        return redirect('project')
    else:
        ctx = {
            "project_delete": project_delete
        }
        return render(request, 'delete_p.html', ctx)



def CommentView(request, com_id):
    form = CommentForm()
    project_com = ProjectModel.objects.get(id=com_id)
    hit_count = get_hitcount_model().objects.get_for_object(project_com)
    count_hits = hit_count.hits
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        count_hits =+ 1
        
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = ProjectModel.objects.get(pk=com_id)
            comment.user_profile = request.user.profile
            comment.user_profile_image = request.user.profile.profile_image
            comment.save()
            
    comm_data = CommentModel.objects.filter(project_id=project_com)
    comment_count = CommentModel.objects.filter(project_id=project_com).count()
    ctx = {
        "project_com": project_com,
        "form": form,
        "com_data": comm_data,
        "comment_count": comment_count,
        "count_hits": count_hits,
    }
    
    return  render(request, 'comment.html', ctx)
    