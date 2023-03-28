import django_filters
from jewellery.models import Diamond

class DiamondFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    
    class Meta:
        model = Diamond
        fields = {
            'shape': ['exact'],
            'carat':['exact'],
            'color': ['exact'], 
            }