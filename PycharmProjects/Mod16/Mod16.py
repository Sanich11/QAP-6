class Product:
	def __init__(self, name, category, quantity_in_stock):
		super(Product, self).__init__()
		self.name = name
		self.category = category
		self.quantity_in_stock = quantity_in_stock
	def is_available(self):
		return True if self.quantity_in_stock > 0 else False

eggs = Product("eggs", "food", 5)
print(eggs.is_available())
