from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, City
from .forms import ProfileForm, PostForm
from django.core.exceptions import PermissionDenied

# home view
def home(request):
    return render(request, 'home.html')

# login redirect to profile home
def profile(request):
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(user = request.user)
    context = {'profile': profile, 'posts': posts}
    return render(request, 'profile/home.html', context)

# sign up view
def signup(request):
    error_message=''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('new_profile')
        else:
            error_message = 'Invalid sign up - please try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

# create profile after user creation
def new_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            new_profile = form.save(commit=False)
            new_profile.user = request.user
            new_profile.save()
            return redirect('user_profile', new_profile.id)
        else:
            return render(request, 'profile/new.html', {'form': form})
    else: 
        form = ProfileForm()
        context = {'form': form}
        return render(request, 'profile/new.html', context)

# view user profile
def user_profile(request, profile_id):
    profile = Profile.objects.get(user = request.user)
    posts = Post.objects.filter(user = request.user)
    context = {'profile': profile, 'posts': posts}
    return render(request, 'profile/home.html', context)

# edit user profile
def edit_profile(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    if request.user == profile.user:
        if request.method == 'POST':
            profile_form = ProfileForm(request.POST, instance=profile)
            if profile_form.is_valid():
                updated_profile = profile_form.save()
                return redirect('profile')
        else:
            form = ProfileForm(instance=profile)
            context = {'form': form}
            return render(request, 'profile/edit.html', context)
    else: 
        raise PermissionDenied("You are not authorized to edit")

# view all destinations
def cities(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'city/index.html', context)

# view a post
def view_post(request, post_id):
    post = Post.objects.get(id=post_id)
    print(post.user)
    context = {'post': post}
    return render(request, 'post/show.html', context)

def view_city(request, city_id):
    city = City.objects.get(id=city_id)
    posts = Post.objects.all().order_by('-timestamp').filter(city_id = city_id)
    post_form = PostForm()
    context = {'city': city, 'posts': posts, 'post_form': post_form}
    return render(request, 'city/show.html', context)

def add_post(request, city_id):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.user = request.user
            new_post.city_id = city_id
            new_post.save()
            return redirect('view_city', city_id)
    else: 
        form = PostForm()
        context = {'form': form, 'city_id': city_id}
        return render(request, 'post/new.html', context)

def delete_post(request, city_id, post_id):
    post = Post.objects.get(id=post_id)
    if request.user == post.user:
        post.delete()
        return redirect('view_city', city_id=city_id)
    else: 
        raise PermissionDenied("You are not authorized to delete")

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)   
    if request.user == post.user: 
        if request.method == 'POST':
            post_form = PostForm(request.POST, instance=post)
            if post_form.is_valid():
                updated_post = post_form.save()
                return redirect('view_post', updated_post.id)
    if request.user == post.user:
        if request.method == 'POST':
            post_form = PostForm(request.POST, instance=post)
            if post_form.is_valid():
                updated_post = post_form.save()
                return redirect('view_post', updated_post.id)
        else: 
            form = PostForm(instance=post)
            context = {'form': form}
            return render(request, 'post/edit.html', context)
    else: 
        raise PermissionDenied("You are not authorized to edit")