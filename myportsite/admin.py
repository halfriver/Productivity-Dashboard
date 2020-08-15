from django.contrib import admin
from .models import TodoList, TodoItem, Board, TodoSubitem, TodoGroup

admin.site.register(TodoList)
admin.site.register(TodoItem)
admin.site.register(Board)
admin.site.register(TodoSubitem)
admin.site.register(TodoGroup)
