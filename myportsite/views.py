from django.views.generic import TemplateView
# copied from https://www.geeksforgeeks.org/python-todo-webapp-using-django/
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import TodoForm
from .models import TodoList, Board, TodoItem

class Index(TemplateView):
    template_name = 'home.html'

def index(request):
    todo_list = TodoList.objects.order_by("-date_submit")
    board_list = Board.objects.all()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    context = {
        "forms" : form,
        "todo_list" : todo_list,
        "board" : board_list,
        "title" : "TODO LIST",
    }
    return render(request, 'home.html', context)

### function to remove item, it recive todo item id from url ##
def remove(request, item_id):
    item = TodoList.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')
