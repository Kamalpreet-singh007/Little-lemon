from django.db import models

# Create your models here.
class Booking_table(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    Booking_date = models.DateTimeField()
    

    def __str__(self):
       return f'{self.title} : {str(self.price)}'

    # def __unicode__(self):
    #     return 
class Menu_table(models.Model):
    Title = models.CharField(max_length =255)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.Title