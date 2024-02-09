from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.http import HttpResponseRedirect, HttpResponse
from .models import User , About, Gallery# Import your User model
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import  UserForm, ContactForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .forms import UserForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse
from django.contrib import messages



def home(request):
    users = User.objects.all().order_by('-id')

    # Define the number of items per page and the maximum visible pages
    items_per_page = 6
    max_visible_pages = 3

    paginator = Paginator(users, items_per_page)
    page = request.GET.get('page')

    try:
        paged_users = paginator.page(page)
    except PageNotAnInteger:
        paged_users = paginator.page(1)
    except EmptyPage:
        paged_users = paginator.page(paginator.num_pages)

    # Calculate the maximum visible page directly in the view
    max_visible_page_calculated = min(paged_users.paginator.num_pages, paged_users.number + max_visible_pages)

    # Calculate visible page numbers
    visible_page_numbers = range(max(1, max_visible_page_calculated - max_visible_pages ), max_visible_page_calculated + 1)

    context = {
        'users': paged_users,
        'visible_page_numbers': visible_page_numbers,
    }

    return render(request, "home.html", context)



class UserDetailView(DetailView):
    model = User
    template_name = 'cmdetails.html'  
    context_object_name = 'user'

def about(request):
     abouts= About.objects.all()
     context={
        'abouts':abouts
    }
     return render(request, 'about.html', context)




def galleryPost(request):
    gallery= Gallery.objects.all().order_by('-id')

    # Define the number of items per page and the maximum visible pages
    items_per_page = 6
    max_visible_pages = 3

    paginator = Paginator(gallery, items_per_page)
    page = request.GET.get('page')

    try:
        paged_gallery = paginator.page(page)
    except PageNotAnInteger:
        paged_gallery = paginator.page(1)
    except EmptyPage:
        paged_gallery = paginator.page(paginator.num_pages)

    # Calculate the maximum visible page directly in the view
    max_visible_page_calculated = min(paged_gallery.paginator.num_pages, paged_gallery.number + max_visible_pages)

    # Calculate visible page numbers
    visible_page_numbers = range(max(1, max_visible_page_calculated - max_visible_pages ), max_visible_page_calculated + 1)

    context = {
        'gallery': paged_gallery,
        'visible_page_numbers': visible_page_numbers,
    }

    return render(request, 'galleryPost.html', context)





def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("ACCOUNT IS DEACTIVATED")
        else:
            return HttpResponse("please use correct id and password")
        
    else:
        return render(request, 'login.html')
    



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))







def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES)
        if user_form.is_valid():
            # Process the form data
            user = user_form.save()
            user.save()
            messages.success(request, 'You have signed up successfully.')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, user_form.errors)
    else:
        user_form = UserForm()
        
    return render(request, 'register.html', {'registered': registered, 'user_form': user_form})




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Create a new Contact instance and save it to the database
            contact = form.save()
            # You can add any additional logic here, such as sending email notifications
            return redirect('home')  # Redirect to a success page
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})



def search(request):
    users = []  # Initialize with an empty queryset
    users_count = 0 
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            users = User.objects.filter(Q(first_name__icontains=keyword) | Q(PPA__icontains=keyword))
            users_count=users.count()
    context = {
        'users': users,
        'users_count':users_count
    }

    return render(request, 'search.html', context)

