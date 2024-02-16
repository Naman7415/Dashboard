from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic import ListView
from myapp.models import Bord
from myapp.forms import MyForm,HomeForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Bondlistview(LoginRequiredMixin,ListView):
    model = Bord
    login_url = 'loginview'
    # redirect_field_name = 'loginview'
    # template_name = 'home.html'
    # success_url = reverse_lazy('home')
    def get(self,request):
        a=request.user
        data=Bord.objects.filter(user=a)
        return render(request, 'home.html',{'data':data})
            
    
class Bondcreateview(LoginRequiredMixin,CreateView):
    login_url = 'loginview'
    model = Bord
    template_name = 'create.html'
    fields = ['title','description','duedate','priority']
    def post(self,request):
        form = HomeForm(request.POST)
        if form.is_valid():
            # a=request.user
            d=form.save(commit=False)
            d.user=request.user
            d.save()
            return redirect('home')
        else:
            form=HomeForm()
        return render(request,self.template_name,{'form':form})
    # template_name = 'create.html'
    # success_url = reverse_lazy('home')
    
class Bondupdateview(UpdateView):
    model = Bord
    fields = ['user','title','description','duedate','priority'] 
    template_name = 'create.html'
    success_url = reverse_lazy('home')
    
class Bonddeleteview(DeleteView):
    model = Bord
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    

class MyFormView(ListView):
    form_class = MyForm
    template_name = "create.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            tt=form.cleaned_data.get('title')
            data=Bord.objects.filter(title__icontains=tt)
            return render(request,'home.html',{'data':data})
        else:
            form=MyForm()
            return render(request, self.template_name, {"form": form})
        
        
##################################################################################
from myapp.forms import UserForm, LogInForm
from django.contrib.auth import login ,authenticate,logout
from django.contrib.auth.hashers import make_password


def singup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.password=make_password(user.password)
            user.save()
            # login(request,aa)
            return redirect('loginview')
    else:
        form = UserForm()
    return render(request,'create.html',{'form':form})

def loginview(request):    
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user=authenticate(username=username,password=password)
            # breakpoint()
            if user:
                login(request,user)
                return redirect('home')
            else:
                ('failed')
    else:
        form = LogInForm()
    return render(request , 'sign_in.html',{'form' :form })

def logoutview(request):
    logout(request)
    return redirect('loginview')

# def pro(request):
#     if request.method == 'POST':
#         form=Proper(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('profunk')    
#     else:
#         form=Proper()
#     return render(request,'create.html',{'form':form})


def profunck(request):
    data={}
    if request.method == 'POST':
        new = request.POST.get('cars')
        a=request.user
        data=Bord.objects.filter(user=a,priority=new)
    
    return render(request,'home.html',{'data':data})

# def vole(request):
#     if request.method =='GET':
#         first=Bord.objects.all() 
#         return render(request,'new.html',{'first':first})
    
    
    
    

# def dropdown(request):
#     if request.method == 'GET':
#         data=Bord.objects.all()
#         print(data)
#         return render(request,'home.html',{'data':data})
        
        
 
 

# def profunck(request):
#     if request.method == 'POST':
#         form=Dropdownform(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data('priority')
#             form.save()
#             return redirect('html')
        
#     else:
#         form=Dropdownform()
#     return render(request,'create.html',{'form':form})