from django.urls import path
from . import views


# sitede gorunecek sekil asagidaki gibi olacak
# www.sitem.com/
# www.sitem.com/todo_detay
# www.sitem.com/todo_ekle

urlpatterns = [
    path('', views.anasayfa, name="anasayfa"),
    path('tododetails/<int:todoId>', views.todoDetail, name="todoDetail"),
    path('todoAdd', views.todoAdd, name="todoAdd"),
    path('remove_todo/<int:todoId>', views.remove_todo, name="remove_todo"),
]
