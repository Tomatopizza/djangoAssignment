from django.contrib import admin
from .models import Product
from .models import Inbound
from .models import Outbound
from .models import Inventory
# Register your models here.
admin.site.register(Inbound) # 이 코드가 나의 UserModel을 Admin에 추가 해 줍니다
admin.site.register(Product)
admin.site.register(Outbound)
admin.site.register(Inventory)