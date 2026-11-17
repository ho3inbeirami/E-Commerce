from django.shortcuts import render
from django.views import View
from django.http import HttpRequest ,HttpResponseRedirect
from django.urls import reverse
from .forms import EditProfileForm, ChangePasswordForm
from account_module.models import *
# Create your views here.


class UserView(View):
    def get(self, request : HttpRequest):
        if request.user.is_authenticated:
            return render(request, 'user_panel/panel.html')
        return HttpResponseRedirect(reverse('login_page'))
    
    
class EditProfileView(View):
    def get(self, request):
        user_id = request.user.id
        user :User = User.objects.filter(id=user_id).first()
        form =EditProfileForm(instance=user)
        context = {
            'form':form,
            'current_user':user
            }
        return render(request,'user_panel/edit_profile.html', context )
    
    def post(self, request):
        user_id = request.user.id
        user :User = User.objects.filter(id=user_id).first()
        form =EditProfileForm(request.POST, request.FILES, instance=user)
        form.save()
        context = {
            'form':form,
            'current_user':user
            }
        return render(request,'user_panel/edit_profile.html', context )
    

class ChangePasswordView(View):
    def get(self, request):
        form = ChangePasswordForm()
        context = {
            'form':form
        }
        return render(request,'user_panel/change_password.html', context )
    
    def post(self, request : HttpRequest):
        user_id = request.user.id
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user = User.objects.filter(id=user_id).first()
            current_password = form.cleaned_data.get('current_password')
            new_password = form.cleaned_data.get('new_password')
        
            if current_user.check_password(current_password):
                current_user.set_password(new_password)
                return HttpResponseRedirect(reverse('home_page'))
            
            
        context = {
            'form':form,
            'errors':'Form data  is invalid'
            }    
        return render(request,'user_panel/change_password.html', context )






