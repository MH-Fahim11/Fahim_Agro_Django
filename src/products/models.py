from django.db import models

class Product(models.Model):
  productname = models.CharField(max_length=255)
  buyingprice = models.IntegerField()
  sellingprice = models.IntegerField()
  totalstock = models.IntegerField()


  def __str__(self):
    return f"{self.productname} "