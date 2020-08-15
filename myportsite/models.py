from django.db import models
from django.utils import timezone

class Board(models.Model):
     name = models.CharField(max_length=30, blank=True, default="New Board", unique=True)
     description = models.TextField(blank=True)

     def __str__(self):
        return self.name

class TodoGroup(models.Model):
    name = models.CharField(max_length=30, blank=True, default="New To-Do")
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TodoList(models.Model):
     name = models.CharField(max_length=30, blank=True, default="New To-Do")
     subtitle = models.CharField(max_length=30, blank=True, default="")
     date_submit = models.DateTimeField(default=timezone.now)
     board = models.ForeignKey(Board, on_delete=models.CASCADE)
     group = models.ForeignKey(TodoGroup, on_delete=models.CASCADE, null=True)

     def __str__(self):
        return self.name

class TodoItem(models.Model):
    name = models.CharField(max_length=30, blank=True, default="")
    date_submit = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    recurring = models.BooleanField(default=False)
    recur_interval = models.DurationField(blank=True, null=True)
    recur_adjust = models.BooleanField(default=False)
    due_ool = models.BooleanField(default=False)
    date_due = models.DateTimeField(blank=True, null=True)
    urgent = models.BooleanField(default=False)
    today = models.BooleanField(default=False)
    overdue = models.BooleanField(default=False)
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class TodoSubitem(models.Model):
    name = models.CharField(max_length=30, blank=True, default="")
    completed = models.BooleanField(default=False)
    urgent = models.BooleanField(default=False)
    item = models.ForeignKey(TodoItem, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
