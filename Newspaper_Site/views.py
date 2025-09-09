from django.shortcuts import render
from accounts.models import Editors
from posts.models import Post, Category
# Create your views here.

def home(request):
    all_news =  []
    category = Category.objects.all()
    categories_with_news = []
    for cata1 in category:
        yes_there_is_atlest_one_news_for_this_cata = Post.objects.filter(categroy=cata1).exists()
        if yes_there_is_atlest_one_news_for_this_cata: categories_with_news.append(cata1)
    
    for cata in categories_with_news:
        all_nwes_for_this_cata = Post.objects.filter(categroy=cata)
        arr = []

        for single_news in all_nwes_for_this_cata:
            arr.append((single_news))
        arr.sort()
        
        all_news.append(arr.pop())
        if len(arr) > 0:
            all_news.append(arr.pop())
        
    return render(request,'index.html',{'all_news': all_news,'category':categories_with_news})


def news_for_a_category(request,pk):
    category =  Category.objects.filter(pk=pk).exists()
    if Category:
        category = Category.objects.all()
        categories_with_news = []
        for cata in category:
           yes_there_is_atlest_one_news_for_this_cata = Post.objects.filter(categroy=cata)
           if   yes_there_is_atlest_one_news_for_this_cata: categories_with_news.append(cata)

        current_cata =  Category.objects.get(pk=pk)
        all_news =  Post.objects.filter(categroy= current_cata)
        arr = []

        for single_news in all_news:
            arr.append((single_news))
        arr.sort()
        arr.reverse()
        if all_news.count()<1:return render(request,'gohome1.html')
        return render(request,'index.html',{'all_news':  arr,'category':categories_with_news})
    
    return render(request,'gohome1.html')