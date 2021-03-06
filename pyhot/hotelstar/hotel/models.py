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

        verbose_name_plural = 'Sastumroebi'

class HotelReview(models.Model):
    review = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    comment = models.TextField()
    star = models.IntegerField()








class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    picture = models.ImageField(upload_to='images', default='images/drug.gif')

    def __str__(self):
        return self.name

    class Meta:

        verbose_name_plural = 'Contact'