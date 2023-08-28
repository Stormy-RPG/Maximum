from django.shortcuts import render
# подключаем объект для выполнения http-запросов
from django.http import HttpResponse
from .models import OnlineShop

# Create your views here.

# функция, отображающая index.html
def index(request):
    # выгружаем все объекты из нашей БД
    online_shops = OnlineShop.objects.all()
    # создаём контекст шаблона
    context = {'online_shops': online_shops}
    return render(request, 'index.html', context)

# функция, отображающая top-sellers.html
def top_sellers(request):
    return render(request, 'top-sellers.html')