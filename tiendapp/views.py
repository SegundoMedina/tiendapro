from django.shortcuts import render

# Create your views here.
def v_index(request):
    context = {
        "products": [None, None, None, None, None]
    }
    return render(request, "tiendapp/index.html", context)

def v_cart(request):
    context = {
        "items": [None, None, None, None]
    }
    return render(request, "tiendapp/cart.html", context)
