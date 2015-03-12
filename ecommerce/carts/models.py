from django.db import models
from products.models import Product, Variation



class CartItem(models.Model):
	cart = models.ForeignKey('Cart', null=True, blank=True)
	product = models.ForeignKey(Product, null=True, blank=True)
	variations = models.ManyToManyField(Variation, null=True, blank=True)
	quantity = models.IntegerField(default=1)
	line_total = models.DecimalField(default=0.00, max_digits=15, decimal_places=2)
	notes = models.TextField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	
	def __unicode__(self):
		try:
			return str(self.cart.id)
		except:
			return self.product.title


class Cart(models.Model):
# items = models.ManyToManyField(CartItem, null=True, blank=True)
# products = models.ManyToManyField(Product, null=True, blank=True)
	total = models.DecimalField(max_digits = 15, decimal_places=2, default=0.00)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=True)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)
	
	def __unicode__(self):
		return "Cart id: %s" %(self.id)

		


