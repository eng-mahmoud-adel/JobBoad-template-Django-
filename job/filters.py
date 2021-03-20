import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='iexact')
    salary = django_filters.NumberFilter()
    salary__gt = django_filters.NumberFilter(field_name='salary', lookup_expr='gt')
    salary__lt = django_filters.NumberFilter(field_name='salary', lookup_expr='lt')
    
    class Meta:
        model = Job
        fields = ['title', 'job_type', 'salary', 'experience', 'category']
