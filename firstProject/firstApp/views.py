from django.http import JsonResponse
from .models import Employee

# Create your views here.
def employeeView(request):
    emp = {
        'id'            : 123,
        'name'          : 'John',
        'sal'        : 100000,
    }
    data                = Employee.objects.all() # Returns a queryset
    response            = {'employees': list(data.values('name', 'sal'))} # Feed the queryset into a dictionary
    return JsonResponse(response)
