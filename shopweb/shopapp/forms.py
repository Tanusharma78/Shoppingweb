from django import forms
from .models import customer, Product

class customerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = ('phone_no', 'bio', 'facebook', 'instagram', 'linkedin', 'image', 'email' ,'address')
     
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name', 'brand','qty','price','category', 'image','description')
        widgets = {
            'product_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Product name'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'description of the Product'}),
            'brand': forms.Textarea(attrs={'class':'form-control', 'placeholder':' Enter Product brand'}),
            'quantity': forms.Textarea(attrs={'class':'form-control'}),
            'price': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Textarea(attrs={'class':'form-control', 'placeholder':'select category'}),
        }