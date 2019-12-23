from django.db import models
from datetime import datetime

# Create your models here.


# models.py altina database olusturmak istiyoruz
class Todo(models.Model):
    baslik = models.CharField(max_length=200)        # kisa birseyse CharField
    metin = models.TextField()                       # uzun birsey yazacaksak burasini kullaniyoruz
    olusturma_tarihi = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):                               # baslik ve yazilari gostermek icin
        return self.baslik



