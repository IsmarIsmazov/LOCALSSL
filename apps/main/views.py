from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from apps.main.models import Category, Promotions
from apps.users.forms import SignIn


# Create your views here.

def main_view(request):
    category = Category.objects.all()
    data = {
        'form': SignIn,
        'category': category

    }
    if request.method == 'GET':
        return render(request, 'layouts/main/index.html', context=data)
    elif request.method == 'POST':
        form = SignIn(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )
            if user:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('username', 'bad request')
        else:
            data = {
                'form': form
            }
            return render(request, 'layouts/main/index.html', context=data)


def about_view(request):
    category = Category.objects.all()

    data = {
        'form': SignIn,
        'category': category

    }
    if request.method == 'GET':
        return render(request, 'layouts/main/about.html', context=data)
    elif request.method == 'POST':
        form = SignIn(data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )
            if user:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('username', 'bad request')
        else:
            data = {
                'form': form
            }
            return render(request, 'layouts/main/about.html', context=data)


# BEAUTY--------------------------------------------------------------------------------------------------------------
class BeautyDetail(DetailView):
    model = Promotions
    template_name = 'layouts/beauty/beauty_detail.html'
    context_object_name = 'beauty'

    def get_queryset(self):
        return Promotions.objects.filter(category__name='Красота и уход')


def beauty(request):
    beauty = Promotions.objects.filter(category__name='Красота и уход')
    return render(request, 'layouts/beauty/beauty.html', {"beautys": beauty})


# Entertainment----------------------------------------------------------------------------------------------------------------
def entertainment(request):
    entertainment = Promotions.objects.filter(category__name='Развличение')
    return render(request, 'layouts/entertainment/entertainment.html', {"entertainments": entertainment})


class EntertainmentDetail(DetailView):
    model = Promotions
    template_name = 'layouts/entertainment/entertainment_detail.html'
    context_object_name = 'entertainment'


# PERSONALITEMS----------------------------------------------------------------------------------------------------------------
def personalitems(request):
    personalitems = Promotions.objects.filter(category__name='Личные вещи')
    return render(request, 'layouts/personalitems/personalitems.html', {"personalitemss": personalitems})


class PersonalitemsDetail(DetailView):
    model = Promotions
    template_name = 'layouts/personalitems/personalitems_detail.html'
    context_object_name = 'personalitems'


# RESTAURANTS----------------------------------------------------------------------------------------------------------------
def restaurants(request):
    restaurants = Promotions.objects.filter(category__name='Кафе и рестораны')
    return render(request, 'layouts/restaurants/restaurants.html', {"restaurantss": restaurants})


class RestaurantsDetail(DetailView):
    model = Promotions
    template_name = 'layouts/restaurants/restaurants_detail.html'
    context_object_name = 'restaurants'


# TRANSPORT----------------------------------------------------------------------------------------------------------------
def transport(request):
    transport = Promotions.objects.filter(category__name='Транспорт')
    return render(request, 'layouts/transport/transport.html', {"transports": transport})


class TransportDetail(DetailView):
    model = Promotions
    template_name = 'layouts/transport/transport_detail.html'
    context_object_name = 'transport'


# REALESTATE----------------------------------------------------------------------------------------------------------------
def realestate(request):
    realestate = Promotions.objects.filter(category__name='Недвижемость')
    return render(request, 'layouts/realestate/realestate.html', {"realestates": realestate})


class RealestateDetail(DetailView):
    model = Promotions
    template_name = 'layouts/realestate/realestate_detail.html'
    context_object_name = 'realestate'
