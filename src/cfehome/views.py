from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators  import staff_member_required
from visits.models import PageVisit
from django.conf import settings



LOGIN_URL =settings.LOGIN_URL




def home_page_view(request, *args ,**kwargs):
    qs=PageVisit.objects.all()
    page_qs=PageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    html_template = "home.html"
    my_context = {
        "page_title": my_title,
        "page_visit_count":page_qs.count(),
        #"percent":(page_qs.count()* 100.0)/qs.count(),
        "total_visit_count":qs.count(),
    }
    path= request.path
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)






def my_old_home_page_view(requests, *args ,**kwargs):
    my_title = "My page"
    my_context = {
        "title": my_title
    }
    html_ ="""

<!DOCTYPE html>
<html>
    <body>
        <h1>{{page_title}} anything ?</h1>
    </body>
</html>
""".format(**my_context)
    return HttpResponse(html_)







VALID_CODE = "abc123"

def pw_protected_view(request, *args, **kwargs):
    is_allowed = False

    if request.method == "POST":
        user_pw_sent = request.POST.get("code")
        if user_pw_sent == VALID_CODE:
            is_allowed = True

    if is_allowed:
        return render(request, "protected/view.html")

    return render(request, "protected/entry.html")









@login_required(login_url=LOGIN_URL)
def user_only_view(request, *args,**kwargs):
    return render(request,"protected/user-only.html",{})



@staff_member_required(login_url=LOGIN_URL)
def staff_only_view(request, *args,**kwargs):
    return render(request,"protected/user-only.html",{})