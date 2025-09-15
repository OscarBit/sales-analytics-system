from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(TimestampedModel):
    name = models.CharField(max_length=255, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Seller(TimestampedModel):
    name = models.CharField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Product(TimestampedModel):
    name = models.CharField(max_length=255, db_index=True)
    category = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Sale(TimestampedModel):
    sale_id = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale_amount = models.DecimalField(max_digits=10, decimal_places=2)
    sale_date = models.DateTimeField(db_index=True)

    def __str__(self):
        return self.sale_id
