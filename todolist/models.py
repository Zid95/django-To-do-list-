from django.db import models
from datetime import datetime, date


class Todo(models.Model):
    todo = models.CharField(max_length=35)
    check_todo = models.BooleanField(default=False)
    datetime = models.DateField(
        auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self) -> str:
        return self.todo
