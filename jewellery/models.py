from django.db import models

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='jewellery/categoryimg', null=True)
    
    def __str__(self) -> str:
        return self.name


class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    color_type = (
        ('Gold','Gold'),
        ('Red','Red'),
        ('Green','Green'),
        ('Blue','Blue'),
        ('Orange','Orange'),
        ('Black','Black'),
        ('Peal','Peal'),
    )
    
    category = models.ForeignKey(Category, on_delete= models.CASCADE, null= True, default="")
    sub_category = models.ForeignKey(Sub_Category, on_delete= models.CASCADE, null= True, default="")
    image = models.ImageField(upload_to='jewellery/pimg')
    name = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=150, default="Meta_title descrpition here")
    desc = models.TextField(default="Descrpition here")
    add_info = models.TextField(default="NO Additonal Info")
    color =  models.CharField(choices=color_type,max_length=10,default="Gold")
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    favourite = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name +" "+ self.sub_category.name + " "+ self.category.name    
    class Meta:
        db_table = "product"
        
        

class Diamond(models.Model):
    shape_type = (
        ('round',' Round'),
        ('princess',' Princess'),
        ('pear',' Pear'),
        ('heart',' Heart'),
        ('asscher',' Asscher'),
        ('cushion',' Cushion'),
        ('oval',' Oval'),
        ('radiant',' Radiant'),
    )
    
    color_type = (
        ('D','D'),
        ('E','E'),
        ('F','F'),
        ('G','G'),
        ('H','H'),
        ('I','I'),
        ('J','J'),
        ('K','K'),
    )
    
    clarity_type = (
        ('FL','FL'),
        ('IF','IF'),
        ('VVS1','VVS1'),
        ('VVS2','VVS2'),
        ('VS1','VS1'),
        ('VS2','VS2'),
        ('SI1','SI1'),
        ('SI2','SI2'),
    )
    
    cut_type = (
        ('H&A','H&A'),
        ('Excellent', 'Excellent'),
        ('V Good','V Good'),
        
    )
    
    symmetry_type = (
        ('Excellent', 'Excellent'),
        ('V Good','V Good'),   
        ('Good','Good'),
    )
    
    image = models.ImageField(upload_to='jewellery/diamondimg')
    name = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=150, default="Meta_title descrpition here")
    desc = models.TextField(default="Descrpition here")
    add_info = models.TextField(default="NO Additonal Info")
    shape =  models.CharField(choices=shape_type,max_length=50,default="round")
    carat = models.FloatField()
    color =  models.CharField(choices=color_type,max_length=10,default="D")
    clarity =  models.CharField(choices=clarity_type,max_length=50,default="FL")
    cut =  models.CharField(choices=cut_type,max_length=50,default="H&A")
    symmetry =  models.CharField(choices=symmetry_type,max_length=50,default="Excellent")
    price = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name 
    
    


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required= True, label= 'Email', error_messages= {'exits': 'This is Already Exists'})

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'


    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_message['exists'])   
        return self.cleaned_data['email'] 