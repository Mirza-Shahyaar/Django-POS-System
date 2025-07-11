from django.shortcuts import render, redirect
from .models import Product, Sale
from django.utils import timezone
from django.contrib import messages
from django.db.models import Sum, DateField
from django.db.models.functions import TruncDate
from django.contrib.auth.decorators import login_required
from django.db import models
from django.db.models import Q 


@login_required
def home_view(request):
    product_count = Product.objects.count()
    sale_count = Sale.objects.count()
    total_revenue = Sale.objects.aggregate(total=models.Sum('total_price'))['total'] or 0

    return render(request, 'posapp/home.html', {
        'product_count': product_count,
        'sale_count': sale_count,
        'total_revenue': total_revenue,
    })

@login_required
def sales_report(request):
    # Group sales by calendar day and sum the totals
    daily_sales = (
        Sale.objects
        .annotate(day=TruncDate('sale_date'))
        .values('day')
        .annotate(total=Sum('total_price'))
        .order_by('-day')           # newest first
    )

    # Prepare data for Chart.js
    labels = [entry['day'].strftime('%Y-%m-%d') for entry in daily_sales]
    totals  = [float(entry['total']) for entry in daily_sales]

    context = {
        'daily_sales': daily_sales,
        'labels': labels,
        'totals': totals,
    }
    return render(request, 'posapp/sales_report.html', context)

# View all products
@login_required
def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(name__icontains=query))
    else:
        products = Product.objects.all()
    return render(request, 'posapp/product_list.html', {'products': products})

# Form to record a sale
@login_required
def sale_form(request):
    products = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product')
        quantity = int(request.POST.get('quantity'))

        product = Product.objects.get(id=product_id)

        if quantity > product.stock:
            messages.error(request, 'Not enough stock available.')
        else:
            total_price = quantity * product.price
            product.stock -= quantity
            product.save()

            Sale.objects.create(
                product=product,
                quantity=quantity,
                total_price=total_price,
                sale_date=timezone.now()
            )

            messages.success(request, f'Sale recorded: {product.name} x{quantity}')
            return redirect('product_list')

    return render(request, 'posapp/sale_form.html', {'products': products})
