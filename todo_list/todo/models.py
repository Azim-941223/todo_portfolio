from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    title = models.CharField('Наименование', max_length=200)
    complete = models.BooleanField('Выполнено', default=False)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title
