from django.shortcuts import render, redirect
from .models import Product, Transaction, Customer
# Create your views here.
def pos_view(request):
    products = Product.objects.all()
    customers = Customer.objects.all()
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        customer_id = request.POST.get('customer_id')
        return redirect('pos_success')
    context = {'products': products, 'customers': customers}
    return render(request, 'sales/sales.html', context)
