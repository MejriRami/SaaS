from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model() 




@login_required
def  profile_list_view(request, *args, **kwargs):
    context={
        "object_list":User.objects.filter(is_active=True)
    }

    return render(request,"profiles/list.html",context)











@login_required 
def profile_view(request,username=None ,  *args, **kwargs):
    print('user.has_perm("auth.view_user")', user.has_perm ("auth.view_user"))
    print('user.has_perm("visits.view_pagevisit")', user. has_perm("visits.view_pagevisit"))
    user =  request.user
    profile_user_obj=get_object_or_404(User, username=username)
    is_me=profile_user_obj==username
    return HttpResponse(f"hello there {username} - {profile_user_obj.id}- {user.id}-{is_me}")  

@login_required
def profile_detail_view(request, username=None, *args, **kwargs):
    user =  request.user
    user_groups=user.groups.all()
    if user_groups.filter(name__icontains="basic").exists():
        return HttpResponse("congrats")
    profile_user_obj=get_object_or_404(User, username=username)
    is_me=profile_user_obj==username
    context={
        "object":profile_user_obj,
        "instance":profile_user_obj,
        "owner":is_me,
    }
    return render(request,"profiles/detail.html",context),