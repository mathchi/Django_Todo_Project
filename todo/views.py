from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def anasayfa(request):

    context = {
        "todos": Todo.objects.all()                  # database models.py deki class ismi Todo oldugu icin bu sekilde yazdik
    }
    return render(request, 'anasayfa.html', context)

def todoAdd(request):
    if request.method == "POST":
        header = request.POST['baslik']
        text = request.POST['metin']                                            # veriyi yollama kontrolu
        
        todo = Todo(baslik=header, metin=text)        # database eklemek icin
        todo.save()

        return redirect('/')                          # islemden sonra yada butona kayittan sonra onceki veya anasayfaya donmesi icin

    return render(request, "todoAdd.html")        # sadece sayfayi yazdiriyor

def todoDetail(request, todoId):

    context = {
        "todo": Todo.objects.get(id=todoId)
    }
    return render(request, "tododetails.html", context)


def remove_todo(request, todoId):                     # database silmek icin                           
    if request.method == "POST":
        todo = Todo.objects.get(id=todoId)            # database eklemek icin
        todo.delete()
        return redirect('/')                          # islemden sonra yada butona kayittan sonra onceki veya anasayfaya donmesi icin

    #return render(request, "tododetails.html")