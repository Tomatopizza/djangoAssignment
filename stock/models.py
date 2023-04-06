from django.db import models

# Create your models here.
# model
class Product(models.Model):
    class Meta:
        db_table = "my_stock"
    """
    무신사 창고관리자는 재고관리를 위한 입출고 시스템을 구성하려고 합니다. 
    쇼핑몰에서는 후드티와 청바지를 판매하고 있습니다. 
    후드티는 기 S, M, L,XL  양말, 모자 Free 사이즈가 있으며 청바지는 Free 사이즈를 판매하고 있습니다. 
    후드티의 종류는 총 3가지가 있으며 각각은 코드번호로 구분합니다. 
    ex) hood-001, hood-002, hood-003 
    청바지 코드는 다음과 같이 구분합니다. ex) jean-001 
    재고는 수정이 가능해야하며 입,출고시 변화하는 수량을 반영할 수 있어야합니다. 
    후드티 3가지?
    양말 1가지
    모자 1가지
    청바지 1가지
    """
    
    """
    상품 모델입니다.
    상품 코드, 상품 이름, 상품 설명, 상품 가격, 사이즈 필드를 가집니다.
    """
    # product = (
    #     ('hood-001', 'Super hood'),
    #     ('hood-002', 'Ultra hood'),
    #     ('hood-003', 'Super Ultra hood'),
    # )
    code = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    price = models.IntegerField(default=0)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1, default='M')
    """
    choices 매개변수는 Django 모델 필드에서 사용하는 매개변수 중 하나로 
    해당 필드에서 선택 가능한 옵션을 지정하는 역할을 합니다. 
    변수를 통해 튜플 리스트를 받으면 첫번째 요소는 실제 DB에 저장되는 값이 되고,
    두번째 요소는 사용자가 볼 수 있는 레이블(옵션의 이름)이 됩니다.
    """



    
    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        self.code = args[0]
        self.name = args[1]
        self.description = args[2]
        self.price = args[3]
        self.sizes = args[4]
        # 생성될 때 stock quantity를 0으로 초기화 로직

# model
class Inbound(models.Model):
    class Meta:
        db_table = "my_inbound"
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    num = models.IntegerField(default=0)
    inbound_date = models.DateTimeField(auto_now_add=True)
    money =  models.IntegerField(default=0)
    """
		입고 모델입니다.
		상품, 수량, 입고 날짜, 금액 필드를 작성합니다.
		"""

# model
class Outbound(models.Model):
    class Meta:
        db_table = "my_outbound"
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    num = models.IntegerField(default=0)
    outbound_date = models.DateTimeField(auto_now_add=True)
    money =  models.IntegerField(default=0)
    """
    출고 모델입니다.
    상품, 수량, 입고 날짜, 금액 필드를 작성합니다.
    """
            
# model
class Invetory(models.Model):
    class Meta:
        db_table = "my_inventory"
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    num = models.IntegerField(default=0)


"""
창고의 제품과 수량 정보를 담는 모델입니다.
상품, 수량 필드를 작성합니다.
작성한 Product 모델을 OneToOne 관계로 작성합시다.
"""