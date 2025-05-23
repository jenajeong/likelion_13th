from django.shortcuts import render

# Create your views here.

def introduce(request):
    nickname = request.GET.get('nickname', 'user') #내가 지정할 수 있는 변수들
    return render(request, 'introduce/home.html', {'nickname': nickname})