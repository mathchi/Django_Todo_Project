from django.contrib import admin
from .models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'baslik', 'metin', 'olusturma_tarihi')   # bu basliklar eklenip panelde gorunsun
    list_display_links = ('id', 'baslik', 'metin')                 # bu basliktakileri tiklanabilir hale getiriyoruz
    list_filter = ('baslik', 'metin')                              # filtreleme fonksiyonu yazmak icin istedigimiz seyi giriyoruz
    search_fields = ('baslik', 'metin', 'id')                      # arama butonu olusturmak icin bunu yapmaliyiz
    list_per_page = 2                                              # herbir listeyi tek sayfada gostermek icin 1 istersek degistirip sayfa icinde linkler koyup todo sayfalarina gecebiliriz
    


admin.site.register(Todo, TodoAdmin)