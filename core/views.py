from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, CreateUserFormLanding, WriteForm, CommentForm
from . import models
from django.core.mail import send_mail

import random

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password incorrect')

        return render(request, 'login/index.html', {})

def logoutUser(request):
    logout(request)
    return redirect('landing')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                messages.success(request,"Hi, " + user + "! Your Eroice account is successfully created! Please Log in.")
                send_mail(
                    '{} registered on eroice!'.format(
                        user
                        ),
                    'username = {}, email = {}.'.format(
                        user,
                        email
                    ),
                    'eroice.id@gmail.com',
                    ['fazirta@gmail.com'],
                    fail_silently=False,
                )
                send_mail(
                    'Welcome to Eroice, {}'.format(
                        user
                        ),
                    '''Thank you for joining Eroice.
Details
username: {}
email: {}
                    '''.format(
                        user,
                        email
                    ),
                    'eroice.id@gmail.com',
                    [email],
                    fail_silently=False,
                )
                return redirect('login')

        context = {
            'form' : form
        }
        return render(request, 'signup/index.html', context)

def landing(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserFormLanding()

        if request.method == 'POST':
            form = CreateUserFormLanding(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                messages.success(request,"Hi, " + user + "! Your Eroice account is successfully created! Please Log in.")
                send_mail(
                    '{} registered on eroice!'.format(
                        user
                        ),
                    'username = {}, email = {}.'.format(
                        user,
                        email
                    ),
                    'eroice.id@gmail.com',
                    ['fazirta@gmail.com'],
                    fail_silently=False,
                )
                send_mail(
                    'Welcome to Eroice, {}'.format(
                        user
                        ),
                    '''Thank you for joining Eroice.
Details
username: {}
email: {}
                    '''.format(
                        user,
                        email
                    ),
                    'eroice.id@gmail.com',
                    [email],
                    fail_silently=False,
                )
                return redirect('login')

        context = {
            'form' : form
        }
        return render(request, 'landing/index.html', context)

class Img_url():
    img_urls = ['https://www.telegraph.co.uk/content/dam/books/2020/10/27/TELEMMGLPICT000242555704_trans_NvBQzQNjv4Bq900leoZVuq6ru6F43OqP_jlaTMTxUhlzF8Rkw038U-A.jpeg', 'https://www.incimages.com/uploaded_files/image/1920x1080/rey-seven-nm-mZ4Cs2I-unsplash_397351.jpg', 'https://dwgyu36up6iuz.cloudfront.net/heru80fdn/image/upload/c_fill,d_placeholder_thenewyorker.png,fl_progressive,g_face,h_1080,q_80,w_1920/v1590006383/thenewyorker_the-oddest-terms-used-for-antique-books-explained.jpg', 'https://assets.teenvogue.com/photos/5e6bffbbdee1770008c6d9bd/16:9/w_2560%2Cc_limit/GettyImages-577674005.jpg', 'https://www.incimages.com/uploaded_files/image/1920x1080/getty_655998316_2000149920009280219_363765.jpg', 'https://images.indianexpress.com/2020/04/books_1200.jpg', 'https://www.incimages.com/uploaded_files/image/1920x1080/getty_883231284_200013331818843182490_335833.jpg', 'https://www.marketplace.org/wp-content/uploads/2021/01/Books_New-e1611252343470.jpg']
    def random(self):
        return random.choice(self.img_urls)

@login_required(login_url='login')
def home(request):
    username = request.user.username
    stories = models.Story.objects.all
    genres = models.Genre.objects.all
    img_url = Img_url()

    return render(request, 'home/index.html', {"username":username, "stories":stories, 'img_url':img_url, 'genres':genres})

@login_required(login_url='login')
def write(request):
    username = request.user.username
    if request.method == 'POST':
        form = WriteForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.user = models.Profile.objects.get(user=request.user)
            stock.save()
            form.save_m2m()
            return redirect('/')
    else:
        form = WriteForm()
    
    genres = models.Genre.objects.all

    context = {
        'form':form,
        'genres':genres,
        "username":username,
    }
    return render(request, 'write/index.html', context)

# https://stackoverflow.com/questions/15407985/django-like-button/15408120
def like(request, story_id):
    new_like, created = models.Like.objects.get_or_create(user=models.Profile.objects.get(user=request.user), story_id=story_id)

def unlike(request, story_id):
    story = get_object_or_404(models.Story, pk=story_id)
    story.like_set.filter(user=models.Profile.objects.get(user=request.user)).delete()

def check_like(request, id):
    story = get_object_or_404(models.Story, pk=id)
    if story.like_set.filter(user=models.Profile.objects.get(user=request.user)).count() == 0:
        return False
    else:
        return True

@login_required(login_url='login')
def story(request, pk_story):
    username = request.user.username
    if request.method == 'POST':
        if request.POST.get('comment'):
            form = CommentForm(request.POST)
            if form.is_valid():
                stock = form.save(commit=False)
                stock.user = models.Profile.objects.get(user=request.user)
                stock.story = models.Story.objects.get(pk=pk_story)
                stock.save()
                return redirect('/story/' + pk_story)
        else:
            if check_like(request, pk_story):
                unlike(request, pk_story)
            else:
                like(request, pk_story)
    else:
        form = CommentForm()

    story = models.Story.objects.get(id=pk_story)
    genres_list = ''
    j = 0
    for i in story.genre.all():
        j+=1
        genres_list += str(i)
        if j != len(story.genre.all()):
            genres_list += ', '
    img_url = Img_url()

    likes = story.like_set.all().count()
    genres = models.Genre.objects.all
    if check_like(request, pk_story):
        like_url = "https://image.flaticon.com/icons/png/512/833/833472.png"
    else:
        like_url = "https://image.flaticon.com/icons/png/512/833/833300.png"

    comments = models.Comment.objects.filter(story=models.Story.objects.get(pk=pk_story))

    context = {
        'story':story,
        'img_url':img_url,
        'genres_list':genres_list,
        'genres':genres,
        'likes':likes,
        'like_url':like_url,
        'form':form,
        'comments':comments,
        "username":username,
    }
    return render(request, 'story/index.html', context)

@login_required(login_url='login')
def literacy(request):
    username = request.user.username
    username = request.user.username
    stories = models.Story.objects.all
    genres = models.Genre.objects.all
    img_url = Img_url()

    return render(request, 'literacy/index.html', {
        'img_url':img_url,
        'genres':genres,
        "username":username,
    })

def handle_not_found(request, exception):
    return render(request, '404/index.html', {})

@login_required(login_url='login')
def genre(request, pk_genre):
    username = request.user.username
    stories = models.Story.objects.all().filter(genre__name=pk_genre)
    genres = models.Genre.objects.all
    img_url = Img_url()

    context = {
        'stories':stories,
        'img_url':img_url,
        'genres':genres,
        "username":username,
    }
    return render(request, 'genre/index.html', context)