from django.shortcuts import render, get_object_or_404, redirect, HttpResponse,HttpResponseRedirect
from .models import Article
from .forms import ArticleCreatedForm, UserLoginForm,UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseBadRequest
import datetime as dt
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


date1 = dt.datetime.now().date()

# Create your views here.
def ArticleList(request):
    query = request.GET.get('search-item')
    article = Article.objects.all()
    
    if query:
        article = Article.objects.filter(
            Q(title__icontains=query) |
            Q(author__username__icontains=query) |
            Q(body__icontains=query)
        )

    paginator = Paginator(article, 4)
    page = request.GET.get('page')

    try:
        article = paginator.page(page)
    except PageNotAnInteger:
        article = paginator.page(1)
    except EmptyPage:
        article = paginator.page(paginator.num_pages)

    return render(request, 'article_list.html', {'article': article})


def Like_Article(request):
    if request.method == 'POST':
        aid = request.POST.get('article_id')
        if not aid:
            return HttpResponseBadRequest("Article ID is required.")
        
        article = get_object_or_404(Article, id=aid)

        if article.likes.filter(id=request.user.id).exists():
            article.likes.remove(request.user)
        else:
            article.likes.add(request.user)

        return HttpResponseRedirect(article.absolute_url())



def ArticleDetails(request, id, slug):
    article = get_object_or_404(Article, id=id)
    is_liked = article.likes.filter(id=request.user.id).exists()  # Check if the user has liked the article

    return render(request, 'details.html', {
        'articles': article,
        'is_liked': is_liked
    })



def CreateArticles(request):
    if request.method == "POST":
        form = ArticleCreatedForm(request.POST)
        if form.is_valid():
            title1 = request.POST.get('title')
            body1 = request.POST.get('body')

            Article(
                title=title1,
                author=request.user,
                created_date=date1,
                body=body1
            ).save()
            return redirect('article_list')
    
        
    else:
        form = ArticleCreatedForm()
        
    
    return render(request, 'create_article.html', {'form': form})

def LOGO(request):
    return render (request,'logo.html')



def UserLogin(request):
    if request.method == "POST":
        loginform = UserLoginForm(request.POST)

        if loginform.is_valid():
            username1 = request.POST.get('username')
            password1 = request.POST.get('password')

            user1 = authenticate(username=username1, password=password1)
            if user1:
                if user1.is_active:
                    login(request, user1)  # Use user1 here
                    return redirect('article_list')
                else:
                    return HttpResponse("Your account is not active")
            else:
                return HttpResponse("You Are Not Allowed To Visit Website")
        else:
            return HttpResponse(f"INVALID DETAILS: {loginform.errors}")
    else:
        form = UserLoginForm()
        return render(request, 'user_login.html', {'form': form})


def LogOut(request):
    logout(request)
    return redirect('article_list')

def UserRegistration(request):
    if request.method == "POST":
        register_form = UserRegistrationForm(request.POST)
        userpass = request.POST.get('password')
        confirmpass = request.POST.get('confirm_password')  # Ensure this field is named 'confirm_password' in the form

        if userpass == confirmpass:  # Check if the passwords match
            if register_form.is_valid():  # Ensure the form is valid
                newuser = register_form.save(commit=False)
                newuser.set_password(register_form.cleaned_data['password'])  # Set the password correctly
                newuser.save()
                return redirect('userlogin')
            else:
                return HttpResponse(f"INVALID FORM DETAILS: {register_form.errors}")
        else:
            return HttpResponse("Passwords do not match.")
    
    else:
        register_form = UserRegistrationForm()
        return render(request, 'rgs.html', {'register_form': register_form})

