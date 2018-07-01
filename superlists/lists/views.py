from django.shortcuts import render, redirect
from lists.models import Item

# 编写视图
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item-text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', { 'items': items })
