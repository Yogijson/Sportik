from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse


class Sport(models.Model):
	sport_name = models.CharField(max_length=250)
	sport_logo = models.FileField()

	def get_absolute_url(self):
		return reverse('theapp:equipment', kwargs={'pk': self.pk})

	def __str__(self):
		return self.sport_name


class Equipment(models.Model):
	sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
	equipment_name = models.CharField(max_length=250)
	equipment_pic = models.FileField()
	price = models.DecimalField(max_digits=10, decimal_places=2, default=None)
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	desc = models.CharField(max_length=1000, default=None)

	def __str__(self):
		return self.equipment_name


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=700)
    contact = models.IntegerField(blank=True,null=True,unique=True)

    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile,sender=User)

class MyCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(UserProfile)
