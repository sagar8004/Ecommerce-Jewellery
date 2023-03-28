from django import forms  
from jewellery.models import Product,Category,Sub_Category,Diamond


class ProductForm(forms.ModelForm):  
    class Meta:  
        model = Product  
        fields = ['category', 'sub_category','image', 'name', 'price','meta_title',]
        

class DiamondForm(forms.ModelForm):  
    class Meta:  
        model = Diamond  
        fields = "__all__"
        
        
# class DiamondFilterForm(forms.Form):
#     name = forms.CharField()