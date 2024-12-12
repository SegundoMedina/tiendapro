from django.shortcuts import redirect, render
from tiendapp.models import Product, ProductCategory

# Create your views here.
def v_index(request):
    products_db = Product.objects.all()

    context = {
        "products": products_db
    }
    return render(request, "tiendapp/index.html", context)

def v_cart(request):
    context = {
        "items": [None, None, None, None]
    }
    return render(request, "tiendapp/cart.html", context)

def v_product_detail(request, code):
    product_obj = Product.objects.get(sku = code)
    rels = ProductCategory.objects.filter(product = product_obj)
    # rels_ids, guarda los ids categoria del producto
    rels_ids = [rr.category.id for rr in rels]
    sug = ProductCategory.objects.filter(
        category__in = rels_ids).exclude(product = product_obj)
    # sug, posee a las sugerencias, pero necesito los ids de los productos
    sug_ids = [ss.product.id for ss in sug]
    extras = Product.objects.filter(id__in = sug_ids)
 
    context = {
        "product": product_obj,
        "extras": extras
    }

    return render(request, 
                  "tiendapp/product_detail.html",
                  context) 

def v_add_to_cart(request, code):
    # Algoritmos nuevos
    # Procesar
    return redirect("/cart")