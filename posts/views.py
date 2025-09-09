from django.shortcuts import render,redirect
from .forms import PostCrationsForm,RatingForm
from.models import Post,Rating,Category
from django.db import IntegrityError
from accounts.models import EditorsProfile

def create_post(request):
    if request.method == 'POST':
        form = PostCrationsForm(request.POST, request.FILES)
        form.instance.editor = request.user.editor_profile
        if form.is_valid():
            form.save()
            request.user.editor_profile. tota_posts+=1
            request.user.editor_profile.save()
            return redirect('home') 
    else:
        form = PostCrationsForm()
        
    return render(request, 'updaloa_a_news.html', {'form': form})

def rate_a_news(request,pk):
    if request.user.is_authenticated:
        user = request.user
        current_post =  Post.objects.filter(pk=pk).exists()
        
        if current_post:
           current_post =  Post.objects.get(pk=pk)
           
           if request.method=='POST':
              form =  RatingForm(request.POST)
              form.instance.user =request.user
              form.instance.post = current_post
              
              if form.is_valid():
                try:
                  form.save()
                  return redirect('home')
                except IntegrityError:
                   return render(request,'gohome.html')
                 
           else:
              form =  RatingForm()
        
        return render(request,'ratingina_nwes.html',{'form':form})
       
    else:
     return redirect('sign_in')
    

def ditials_view(request,pk):
   single_news = Post.objects.get(pk=pk)
   single_news.viwes_of_this+=1
   single_news.save()
   cata_gory_now = single_news.categroy
   all_news = Post.objects.filter(categroy=cata_gory_now)
   all_rating_for_this_news = Rating.objects.filter(post=single_news)
   category = Category.objects.all()
   categories_with_news = []
   ralated_nwes=[]
   for i in all_news:
       if i != single_news and len(ralated_nwes)<2:
            ralated_nwes.append(i)
       if len(ralated_nwes)>1:break

   for cata in category:
           yes_there_is_atlest_one_news_for_this_cata = Post.objects.filter(categroy=cata)
           if   yes_there_is_atlest_one_news_for_this_cata: categories_with_news.append(cata)

   return render(request,'newsditala.html',{'single_news':single_news,'all_rating_for_this_news': all_rating_for_this_news,'category':categories_with_news,'ralated_nwes':ralated_nwes})


def search_news(request):
     if request.method == 'POST':
        key_word = request.POST['search_query']
        nwes_for_this_serch =  Post.objects.filter(headline__contains=key_word)

     category = Category.objects.all()
     categories_with_news = []
     for cata in category:
           yes_there_is_atlest_one_news_for_this_cata = Post.objects.filter(categroy=cata)
           if   yes_there_is_atlest_one_news_for_this_cata: categories_with_news.append(cata)
     return render(request,'index.html',{'all_news': nwes_for_this_serch,'category':categories_with_news})
        
   
def delete_a_post(request,pk):
   current_post=Post.objects.get(pk=pk)
   current_post.delete()
   editor   = EditorsProfile.objects.get(user=request.user)
   if editor.tota_posts>0:
       editor.tota_posts-=1
       editor.save()
   return redirect('all_of_a_editor')


def update_a_post(request,pk):
   current_post=Post.objects.get(pk=pk)
   if request.method=='POST':
       form = PostCrationsForm(request.POST, request.FILES,instance= current_post)
       if form.is_valid():
          form.save()
       return redirect('all_of_a_editor')
               
   else:
      form=PostCrationsForm(instance= current_post)
   
   return render(request, 'updaloa_a_news.html', {'form': form})