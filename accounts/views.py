from django.shortcuts import render,redirect
from.forms import SignupForm,UserLoingForm,UserProfileUpdate,EditorApplyForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from.models import Editors,EditorsProfile,ApplicationsForEditors
from posts.models import Post
# Create your views here.

def singup(request):
   if request.method=='POST':
      form=SignupForm(request.POST)
      
      if form.is_valid():
         user = form.save()
         messages.success(request, 'Successfully signed up!')
         login(request,user)
         return redirect('see_my_profie')
   else:
      form=SignupForm()
   
   return render (request,'user_register.html',{'form':form})

def sign_in(request):
   if request.method=='POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username= username, password= password)
      if user is not None:
          messages.success(request, 'Successfully signed in !')
          login(request,user)
          return redirect('see_my_profie')
      else: messages.error(request, 'correct the usernama or password !')

   else:
      form=UserLoingForm()
   
   return render (request,'user_Login.html')


def see_my_profie(request):
   yes_he_made_application = ApplicationsForEditors.objects.filter(user = request.user).exists()
   yes_editor = Editors.objects.filter(user_name = request.user.username).exists()
   return render(request,'user_profile.html',{'yes_editor':yes_editor,'yes_he_made_application': yes_he_made_application})


def edit_my_profile(request):
   if request.method=="POST":
      form = UserProfileUpdate(request.POST, instance=request.user)
      if form.is_valid():
         user = form.save()
         messages.success(request, 'Successfully updated your profile')
         login(request,user)
         return redirect('see_my_profie')
      else:messages.error(request, 'correct the following fields!')
   
   else: form = UserProfileUpdate(instance=request.user)
   return render(request,'update_general_user_profile.html',{'form':form})


def change_my_password(request):
    if request.method=='POST':
        print('here>>101')
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user) 
            messages.success(request, 'successfully updated!!!!!')
            return redirect('see_my_profie')
        else:
            messages.error(request, 'something went wrong')
    else:
       form = PasswordChangeForm(request.user)

    return render(request,'password_change.html',{'form':form})


def apply_as_editors(request):
   if request.method=='POST':
     form = EditorApplyForm(request.POST)
     form.instance.user =request.user
     if form.is_valid():
        form.save()
        messages.success(request, 'successfully applyed!!!!!')
        return redirect('see_my_profie')
     else:
        messages.success(request, 'something wrong !!!!!')

   else:
      form = EditorApplyForm()

   return render (request,'editor_apply.html',{'form':form})


def Logout(request):
    logout(request)
    return redirect('home')


def edotor_profile(request):
      yes_editor = Editors.objects.filter(user_name = request.user.username).exists()
      return render(request,'edtior_profile.html',{'yes_editor':yes_editor,})

def all_of_a_editor(request):
      my_editor_id = EditorsProfile.objects.get(user = request.user)
      my_all_post= Post.objects.filter(editor=my_editor_id)
      return render(request,'post_for_editor.html',{'my_all_post':my_all_post})