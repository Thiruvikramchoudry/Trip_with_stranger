from django.db import models

# Create your models here.

class comments(models.Model):
    username = models.CharField(max_length=20)
    user_email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.username

class registration(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20,primary_key=True)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    user_email = models.EmailField(max_length=40)
    mobile_number = models.CharField(max_length=12)
    password = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    #user_image=models.ImageField(null=True,blank=True, upload_to="user_images/")
    image_url=models.CharField(max_length=100)

    def __str__(self):
        return self.username

class slot_details(models.Model):
    username=models.CharField(max_length=20)

    slotname = models.CharField(max_length=30)
    Arrivalcity = models.CharField(max_length=30)
    Destination = models.CharField(max_length=30)
    Days_of_Trip = models.IntegerField()
    Current_Number_Members=models.IntegerField()
    Number_of_Members = models.IntegerField()
    slot_id=models.IntegerField()
    Minimum_age_Members = models.IntegerField()
    Maximum_age_Members = models.IntegerField()
    Total_Male = models.IntegerField()
    Total_Female = models.IntegerField()
    Starting_Date = models.CharField(max_length=10)
    Returning_Date = models.CharField(max_length=10)
    Current_Number_Male=models.IntegerField()
    Current_Number_Female = models.IntegerField()

    def __str__(self):
        return self.slotname


class user_with_slotdetail(models.Model):
    username=models.CharField(max_length=20)
    slot_id=models.IntegerField()
    def __str__(self):
        return self.username
