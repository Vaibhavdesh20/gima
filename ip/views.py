from django.shortcuts import render, redirect , HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required 
from .models import iplist
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.template import loader
from .forms import iplistForm
from django.db.models import Q
from django.views.generic import  ListView
from django.template import loader
from django.urls import reverse


# Create your views here.

def login(request):
    if request.session.has_key('is_logged'):
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)


        if user is not None:

            auth.login(request, user)
            request.session['is_logged'] = True
            return redirect('home')
        else:
            messages.info(request, 'invalid user name or password')
            return redirect('login')

    else:
        return render(request, 'login.html')

def logout(request): 
    auth.logout(request)
    return redirect('login')
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user=auth.authenticate(username=username,password=password)

#         if user is not None:
#             auth.login(request,user)
#             # messages.success(request,'YOU ARE Logged In')
#             #teams = Team.objects.all()
#             return redirect('home',) # after login you want to open page you maintion there
#         else:
#             messages.warning(request,'Invalid Credentials')
#             return redirect('login')# Jr user login id / pass galt zala tr kontya page la thevayche
    
#     return render(request,'login.html')

# @login_required(login_url='login')
# def logout_user(request):
#     logout(request)
#     # messages.success(request,'Logout')
#     return redirect('login')# return page after logout click



@login_required(login_url='login')
def home(request):
    iplists = iplist.objects.all()
    data = {
          'iplists' : iplists,
    }
    return render(request, 'home.html',data)

@login_required(login_url='login')
def add_ip(request):
    submitted = False
    if request.method == "POST":
        form = iplistForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Add IP SuccessFul')
            return HttpResponseRedirect('./add_ip?submitted=True')
    else:
        form = iplistForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'add_ip.html',{'form':form, 'submitted':submitted})


class SearchResultsView(ListView):
    model = iplist
    template_name = "search_results.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = iplist.objects.filter(
            Q(group__icontains=query) | Q(ip_address__icontains=query) | Q(site__icontains=query) | Q(dept__icontains=query) | Q(user_name__icontains=query) | Q(mac_address__icontains=query)
        )
        return object_list
        


@login_required(login_url='login')
def update(request,Iplist_id):
    Iplist = iplist.objects.get(pk=Iplist_id)
    form = iplistForm(request.POST or None, instance=Iplist)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request,'update.html',{'Iplist' : Iplist,'form':form})

def edit_ip(request):
    iplists = iplist.objects.all()
    data = {
          'iplists' : iplists,
    }
    return render(request,'edit_ip.html',data)

def delete_ip(request):
    iplists = iplist.objects.all()
    data = {
          'iplists' : iplists,
    }
    return render(request,'delete_ip.html',data)

@login_required(login_url='login')
def delete(request, Iplist_id):
    Iplist = iplist.objects.get(pk=Iplist_id)
    Iplist.delete()
    messages.success(request,'Record Delete')
    return redirect('home')

# def delete(request, iplist_id):
#   Iplists = iplist.objects.get(iplist_id)
#   Iplists.delete()
#   return HttpResponseRedirect(reverse('home.html'))

# def update(request, id):
    # iplists = iplist.objects.get(id=id)
    # template = loader.get_template('update.html')
    # context = {
    #     'iplists': iplists,
    # }
    # return HttpResponse(template.render(context, request))



# def Iplist(request):
#     if request.method == 'POST':
#         group = request.POST['group']
#         ip_address = request.POST['ip_address']
#         site = request.POST['site']
#         dept = request.POST['dept']
#         user_name = request.POST['user_name']
#         mac_address = request.POST['mac_address']
        

#         #  do all sanitization
#         Iplist = iplist(group=group, ip_address=ip_address, site=site, dept=dept,
#                               user_name=user_name, mac_address=mac_address)
#         Iplist.save()
#         messages.success(request, 'Add data Sucessful!')
#         return HttpResponseRedirect('/iplist?submitted=True')