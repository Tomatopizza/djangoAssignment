from django.db import models

# Create your models here.
# model
class Product(models.Model):
    class Meta:
        db_table ="my_product"
    
    codes = (
        ('hood1', 'fancy hood'),
        ('hood2', 'pretty hood'),
        ('hood3', 'hice hood'),
        ('socks', 'socks'),
        ('jeans', 'new jeans'),
    )
    name = models.CharField(default = 'fancy hood',max_length=100)
    description = models.TextField(default = "write anything")
    price = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    code = models.CharField(choices=codes, default='hood1', max_length=5)
    size = models.CharField(choices=sizes, max_length=1)
    """
    상품 모델입니다.
    상품 코드, 상품 이름, 상품 설명, 상품 가격, 사이즈 필드를 가집니다.
    """
'''
    code = 
    name = 
    description = 
    price = 
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )

    size = models.CharField(choices=sizes, max_length=1)
		"""
		choices 매개변수는 Django 모델 필드에서 사용하는 매개변수 중 하나로 
		해당 필드에서 선택 가능한 옵션을 지정하는 역할을 합니다. 
		변수를 통해 튜플 리스트를 받으면 첫번째 요소는 실제 DB에 저장되는 값이 되고,
		두번째 요소는 사용자가 볼 수 있는 레이블(옵션의 이름)이 됩니다.
		"""

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        # 생성될 때 stock quantity를 0으로 초기화 로직
'''
# model
class Inbound(models.Model):
    class Meta:
        db_table ="my_inbound"
    product = models.OneToOneField("Product", on_delete=models.CASCADE)
    num = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)


class Outbound(models.Model):
    class Meta:
        db_table ="my_outbound"
    product = models.OneToOneField("Product", on_delete=models.CASCADE)
    num = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)

class Inventory(models.Model):
    class Meta:
        db_table ="my_inventory"
    product = models.OneToOneField("Product", on_delete=models.CASCADE)
    num = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    total_inbound = models.IntegerField(default=0)
    total_outbound = models.IntegerField(default=0)
    
    
    """
		입고 모델입니다.
		상품, 수량, 입고 날짜, 금액 필드를 작성합니다.
		"""
'''
# model
class Outbound(models.Model):
		"""
		출고 모델입니다.
		상품, 수량, 입고 날짜, 금액 필드를 작성합니다.
		"""
                
# model
class Invetory(models.Model):
	"""
	창고의 제품과 수량 정보를 담는 모델입니다.
	상품, 수량 필드를 작성합니다.
	작성한 Product 모델을 OneToOne 관계로 작성합시다.
	"""
'''