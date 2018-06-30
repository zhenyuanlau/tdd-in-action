from django.shortcuts import render

# 编写视图
def home_page(request):
    return render(request, 'home.html')
