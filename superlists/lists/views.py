from django.shortcuts import render, redirect
from lists.models import Item, List

# 编写视图
def home_page(request):
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', { 'items': items })

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item-text'], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
    return redirect('/lists/the-only-list-in-the-world/')
