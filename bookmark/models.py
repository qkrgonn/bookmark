from django.db import models
from django.urls import reverse
# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def __str__(self):
        return "이름 : "+self.site_name + ", urls : "+self.url
