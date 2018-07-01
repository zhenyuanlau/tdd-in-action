from django.shortcuts import render, redirect
from lists.models import Item

# 编写视图
def home_page(request):
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', { 'items': items })

def new_list(request):
    Item.objects.create(text=request.POST['item-text'])
    return redirect('/lists/the-only-list-in-the-world/')
    return redirect('/lists/the-only-list-in-the-world/')
