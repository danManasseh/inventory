from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Home, City, Item
from .forms import itemForm, homeForm
from django.db.models import Q
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
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    homelist = Home.objects.filter(
        Q(city__name__startswith = q) |
        Q(name__startswith = q)
    )
    # itemList = Item.objects.filter(Q(name__startswith = q))
    context = {'homelist':homelist,'q':q}
    return render(request, 'base/index.html', context)


##dashboard page
@login_required(login_url='login')
def homeitemPage(request, pk):
    home = Home.objects.get(id = pk)
    items = home.item_set.all().order_by('-created')
    context = {'items':items, 'home':home}
    return render(request, 'base/dashboard.html', context)


##items page
@login_required(login_url='login')
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
    context = {'form':form}
    return render(request, 'base/add-item.html', context)


#item-detail
@login_required(login_url='login')
def itemDetails(request, pk):
    item = Item.objects.get(id = pk)
    context = {'item':item}
    return render(request, 'base/item-detail.html', context)


#update Item
# @login_required(login_url='login')
def updtateItem(request, pk):
    item = Item.objects.get(id = pk)
    form = itemForm(instance= item)

    if request.method == 'POST':
        form = itemForm(request.POST, request.FILES, instance = item)
        if form.is_valid():
            temp_form = form.save(commit=False)
            temp_form.name = temp_form.name.lower()
            temp_form.save()
            return redirect('home-item', pk = item.home_name.id)

    context = {'form':form, 'item':item}
    return render(request, 'base/add-item.html', context)

# @login_required(login_url='login')
def deleteItem(request, pk):
    item = Item.objects.get(id = pk)
    temp = item

    if request.method == 'POST':
        item.delete()
        return redirect('home-item', pk = temp.home_name.id)
    return render(request, 'base/delete.html', {'obj':item})


# @login_required(login_url='login')
def addHome(request):
    form = homeForm()
    cities = City.objects.all()

    if request.method == 'POST':
        city_name = request.POST.get('city')
        city, created = City.objects.get_or_create(name = city_name)
        Home.objects.create(
            name = request.POST.get('name'),
            city = city,
            house_pic = request.FILES.get('house_pic')
        )
        return redirect('home')

    context = {'form':form, 'cities':cities}
    return render(request, 'base/add-home.html', context)

# @login_required(login_url='login')
def updateHome(request, pk):
    home = Home.objects.get(id = pk)
    form = homeForm(instance=home)
    cities = City.objects.all()

    if request.method == 'POST':
        city_name = request.POST.get('city')
        city, created = City.objects.get_or_create(name = city_name)
        form = homeForm(request.POST, request.FILES, instance=home)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.city = city
            temp.save()
            return redirect('home')

    context = {'form':form,'cities':cities}
    return render(request, 'base/add-home.html', context)