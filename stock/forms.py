from . import models

# form

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'description', 'price', 'size']
        
# form
class InboundForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'code', 'description', 'price', 'size']
		"""
		Django로 개발을 할때,
		Model과 Form을 사용하지 않으면 Django를 사용하는 의미가 없다고 말할 정도로 
		Model과 Form은 Django의 핵심 기능 입니다. 
		Form의 사용방법을 익혀 봅시다.
		"""

# form
class OutboundForm(forms.ModelForm):
     pass