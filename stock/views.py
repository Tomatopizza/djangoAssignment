from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .models import Inbound
from .models import Outbound
from .models import Inventory
from django.db.models import Q
def inbound(request):
    if request.method == 'GET':
        all_product = Product.objects.all()
        return render(request, 'stock/inbound.html', {'inbound': all_product})
    elif request.method == 'POST':
        
        number = request.POST.get('number',None)
        code = request.POST.get('code',None)
        size = request.POST.get('size',None)
        all_product = Product.objects.all()
        all_inbound = Outbound.objects.all()
        code_inbound = all_inbound.get(product=size_proudct)
        # size_inbound = code_inbound.get(size=size)
        code_proudct = all_product.filter(Q(code=code))
        size_proudct = code_proudct.get(size=size)
        code_inbound.num += int(number)
        size_proudct.num += int(number)
        size_proudct.save()
        code_inbound.save()
        all_product = Product.objects.all()
        return render(request, 'stock/inbound.html', {'inbound': all_product})
        
def outbound(request):
    if request.method == 'GET':
        all_product = Product.objects.all()
        return render(request, 'stock/outbound.html', {'outbound': all_product})
    elif request.method == 'POST':
        number = request.POST.get('number',None)
        code = request.POST.get('code',None)
        size = request.POST.get('size',None)
        all_outbound = Outbound.objects.all()
        all_product = Product.objects.all()
        
        code_proudct = all_product.filter(Q(code=code))
        size_proudct = code_proudct.get(size=size)
        print(size_proudct)
        code_outbound = all_outbound.get(product=size_proudct)
        #size_outbound = code_outbound.get()
        if size_proudct.num < int(number):
            return HttpResponse("Too Many!")
        size_proudct.num -= int(number)
        code_outbound.num += int(number)
        size_proudct.save()

        code_outbound.save()
        all_product = Product.objects.all()
        return render(request, 'stock/outbound.html', {'outbound': all_product})

def inventory(request):
    if request.method == 'GET':
        all_outbound = Outbound.objects.all()
        all_inbound = Inbound.objects.all()
        all_product = Product.objects.all()
        total_outbound_price = 0
        total_inbound_price = 0
        for i in all_outbound:
            for j in range(i.num):
                total_outbound_price += i.price
        for i in all_inbound:
            for j in range(i.num):
                total_inbound_price += i.price
        return render(request, 'stock/inventory.html',  context={'outbound': all_outbound, 'inventory': all_product, 'inbound': all_inbound, 'total_outbound_price': total_outbound_price, 'total_inbound_price': total_inbound_price})
    elif request.method == 'POST':
        all_outbound = Outbound.objects.all()
        # code_outbound = all_outbound.filter(Q(code=code))
        # size_outbound = code_outbound.get(size=size)
        all_inbound = Inbound.objects.all()
        # code_inbound = all_inbound.filter(Q(code=code))
        # size_inbound = code_inbound.get(size=size)
        all_product = Product.objects.all()
        return render(request, 'stock/inventory.html', context={'outbound': all_outbound, 'inventory': all_product, 'inbound': all_inbound})


        # do update
# Create your views here.
        

# Create your views here.
# view
'''
@login_required
def product_list(request):
	if request.method == 'GET':
	    pass
        # return render(request, 'user/signup.html')
    elif request.method == 'POST':
        pass
	pass
    # 등록 된 상품의 리스트를 볼 수 있는 view

@login_required
def product_create(request):
	if request.method == 'GET':
	    pass
        # return render(request, 'user/signup.html')
    elif request.method == 'POST':
        code = request.POST.get('code', None)
        name = request.POST.get('name',None)
        description = request.POST.get('description',None)
        price = request.POST.get('price',None)
        sizes = request.POST.get('sizes',None)
        # 여기에 None이 없다면 추가 필요 #######################
        product_created = Product()
        product_created.code = code
        product_created.name = name
        product_created.description = description
        product_created.price = price
        product_created.sizes = sizes
        product_created.save()

    # 상품 등록 view

# view
@login_required
@transaction.atomic
def inbound_create(request):
	if request.method == 'GET':
	    pass
        # return render(request, 'user/signup.html')
    elif request.method == 'POST':
        product_code = request.POST.get('product', None)    
        num = request.POST.get('num',None)
        # inbound_date = request.POST.get('inbound_date',None)
        money = request.POST.get('money',None)
        # 여기에 None이 없다면 추가 필요 #######################
        inbound_created = Inbound()
        inbound_created.product = product
        #inbound_created.num = num
        # inbound_created.inbound_date = inbound_date
        # inbound_created.money = money
        inbound_created.save()
    # 상품 입고 view
    # 입고 기록 생성
    
		# 입고 수량 조정

@login_required
def outbound_create(request, product_id):
	if request.method == 'GET':
	    pass
        # return render(request, 'user/signup.html')
    elif request.method == 'POST':
        num = request.POST.get('num',None)
        # outbound_date = request.POST.get('outbound_date',None)
        money = request.POST.get('money',None)
        # 여기에 None이 없다면 추가 필요 #######################
        outbound_created = Outbound()
        outbound_created.product.code = product_id
        outbound_created.num = num
        # outbound_created.outbound_date = outbound_date
        outbound_created.money = money
        outbound_created.save()
        # exist_inventory = Inventory.objects.get(product_id=product.code)
        # exist_inventory.num -= outbound_created.num

		# 상품 출고 view
    # 출고 기록 생성
    
		# 재고 수량 조정

# view
@login_required
def inventory(request): #어떻게 해야할지 감이 잘 안잡힘.
	if request.method == 'GET':
	    inbound_items = Inbound.objects.all()
	    outbound_items = Outbound.objects.all()
	    return render(request, 'stock/inventory.html')
	    
        # return render(request, 'user/signup.html')
    elif request.method == 'POST':
        pass


        # 여기에 None이 없다면 추가 필요 #######################
        # inventory_created = Inventory()
        # inventory_created.product = product
        # inventory_created.num = num
        # inventory_created.save()
	"""
	inbound_create, outbound_create view에서 만들어진 데이터를 합산합니다.
	Django ORM을 통하여 총 수량, 가격등을 계산할 수 있습니다.
	"""
	# 총 입고 수량, 가격 계산

	# 총 출고 수량, 가격 계산

'''

def calculate(request):
    if request.method == 'GET':
        return render(request, 'calc.html')
    elif request.method == 'POST':
        number = request.POST.get('number',None)
        number = int(number)
        exist_calc = Calculator.objects.get()
        exist_calc.num += number
        result = exist_calc.num
        exist_calc.save()
        return render(request, 'inbound.html', {'inbound': result})