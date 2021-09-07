from django.db import models
from django.db.models.manager import Manager
# from django.db.models.fields import IntegerField


# id, name, qty, price, is_published, author ....superuser/ admin pass:- Kiran@123

class ActiveBookManager(models.Manager):
    def get_queryset(self):
	    return super().get_queryset().filter(is_deleted="N")


class InActiveBookManager(models.Manager):
    def get_queryset(self):
	    return super().get_queryset().filter(is_deleted="Y")        

#class is defined below 
"""this is class named Book is defined"""
class Book(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
    is_deleted = models.CharField(max_length=1, default="N") # try with 0 and 1 instead of N
    active_books = ActiveBookManager()
    inactive_books = InActiveBookManager()
    objects = Manager()

    def __str__(self):
        return f"{self.__dict__}"

    class Meta:
        db_table = "book"
