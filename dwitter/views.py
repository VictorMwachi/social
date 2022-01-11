# dwitter/views.py

from django.shortcuts import render
from .models import Profile,Dweet

def dashboard(request):
    return render(request, "base.html")
    

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    if request=='POST':
        current_user_profile=request.user.profile
        data=request.POST
        action=data.get('follow')

        if action=='follow':
            current_user_profile.follows.add(profile)
        
        elif action=='unfollow':
            current_user_profile.follows.remove(profile)

        current_user_profile.save()
        
    return render(request, "dwitter/profile.html", {"profile": profile})

# def post(request):
#     post=Post.objects.get(pk=pk)
#     return render(request,"dwitter/posts.html",{"post":post})