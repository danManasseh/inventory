from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Home, City, Item
from .forms import itemForm
# Create your views here.


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')        
    return render(request, 'base/login.html')

def logoutPage(request):
    logout(request)
    return redirect ('login')

@login_required(login_url='login')
def home(request):
    homelist = Home.objects.all()
    context = {'homelist':homelist}
    return render(request, 'base/index.html', context)


##dashboard page
def homeitemPage(request, pk):
    home = Home.objects.get(id = pk)
    items = home.item_set.all().order_by('-created')
    context = {'items':items, 'home':home}
    return render(request, 'base/dashboard.html', context)


##items page
def additemPage(request, pk):
    home = Home.objects.get(id = pk)
    form = itemForm()
    if request.method == 'POST':
        form = itemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.name = item.name.lower()
            item.home_name = home
            item.save()
            return redirect('home-item', pk = home.id)
        # Item.objects.create(
        #     name = request.POST.get('item_name'),
        #     item_img = request.FILES('item_pic'),
        #     quantity = request.POST.get('item_quantity'),
        #     home_name = home,
        # )
    context = {'form':form}
    return render(request, 'base/add-item.html', context)