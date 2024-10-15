from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def merchandise_list(request):
    products = Product.objects.all()
    return render(request, 'merchandise/merchandise_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.order_by('-created_at')
    return render(request, 'merchandise/product_detail.html', {'product': product, 'reviews': reviews})

@login_required
def add_review(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(
                product=product,
                user=request.user,
                rating=form.cleaned_data['rating'],
                title=form.cleaned_data['title'],
                body=form.cleaned_data['body']
            )
            return redirect('product_detail', pk=product.pk)
    else:
        form = ReviewForm()
    return render(request, 'merchandise/add_review.html', {'form': form, 'product': product})