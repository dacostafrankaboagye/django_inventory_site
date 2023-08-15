
from django.db import models
from django.contrib.auth.models import User


CATEGORY = (

	('Stationary', 'Stationary'),
	('Electronics', 'Electronics'),
	('Food', 'Food'),


)

# Create your models here.
class Product(models.Model):
	# the properties
	name = models.CharField(max_length=100, null=True)
	category = models.CharField(max_length=20, choices=CATEGORY, null=True)
	quantity = models.PositiveIntegerField(null=True)


	# changing the default namme (Products) to say, Product
	class Meta:
		verbose_name_plural = 'Product'

	#it appears exactly as we want it
	def __str__(self):
		return f'{self.name}-{self.quantity}'



class Order(models.Model):
	# foreign key-> many to one relationship
	# many orders for one product
	# many orders will come from a staff
	# if a product is deleted, there should not be any relationship with an order
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	# any order can come from a staff
	staff = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	order_quantity = models.PositiveIntegerField(null=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.product} ordered by {self.staff.username}'
	
