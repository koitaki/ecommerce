from django.contrib import admin

# Register your models here.
from products.models import Product, ProductImage, Variation

class ProductAdmin(admin.ModelAdmin):

	# Dates at Top
	date_hierarchy = 'timestamp'

	# Search Fields
	search_fields = ['title', 'description']

	# Fields Displayed
	list_display = ['title', 'price', 'active', 'updated']
	list_editable = ['price', 'active']

	# Filters
	list_filter = ['price', 'active']
	
	# Read-only Fields (note these are fields with Auto)
	readonly_fields = ['updated', 'timestamp']

	# Prepopulated Fields
	prepopulated_fields = {'slug': ('title',)}


	class Meta:
		model = Product


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)

admin.site.register(Variation)

