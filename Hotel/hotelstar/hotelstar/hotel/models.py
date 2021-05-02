from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    stars = models.IntegerField()
    price = models.IntegerField()
    picture = models.ImageField(upload_to='images', default="images/124180566_3771168516249284_3976912378791517206_o.jpg")
    HOTEL_TYPE = (
        ("1", "Free WiFi"),
        ("2", "No WiFi"),
    )
    HOTEL_TYPE2 = (
        ("1", "Free Parking"),
        ("2", "No Parking")
    )

    hotel_type = models.CharField(max_length=128, default="1", choices=HOTEL_TYPE)
    hotel_type2 = models.CharField(max_length=128, default=1, choices=HOTEL_TYPE2)



    def __str__(self):
        return self.name + " | " + str(self.stars) + " Stars"

    class Meta:

        verbose_name_plural = 'Hotels'



class HotelReview(models.Model):
    review = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=128, null=True)
    email = models.EmailField(max_length=128, null=True)
    comment = models.TextField(max_length=1000, null=True)
    RATING_NUMBER = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),

    )

    rating_number = models.CharField(max_length=128, default="5", choices=RATING_NUMBER, null=True)
    picture = models.ImageField(upload_to='images', default="bendu.jpg", null=True)
    permission = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)

    class Meta:

        verbose_name_plural = 'Reviews'




class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    picture = models.ImageField(upload_to='images', default='images/drug.gif')

    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = 'Contacts'


class Test(models.Model):
    name = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)

