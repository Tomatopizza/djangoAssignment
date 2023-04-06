# view
@login_required
def product_list(request):
    # 등록 된 상품의 리스트를 볼 수 있는 view

@login_required
def product_create(request):
    # 상품 등록 view

# view
@login_required
@transaction.atomic
def inbound_create(request):
    # 상품 입고 view
    # 입고 기록 생성
    
		# 입고 수량 조정

@login_required
def outbound_create(request, product_id):
		# 상품 출고 view
    # 출고 기록 생성
    
		# 재고 수량 조정

# view
@login_required
def inventory(request):
	"""
	inbound_create, outbound_create view에서 만들어진 데이터를 합산합니다.
	Django ORM을 통하여 총 수량, 가격등을 계산할 수 있습니다.
	"""
	# 총 입고 수량, 가격 계산

	# 총 출고 수량, 가격 계산