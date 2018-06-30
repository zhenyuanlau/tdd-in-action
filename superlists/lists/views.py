from django.shortcuts import render
from django.http import HttpResponse

# 编写视图
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')
