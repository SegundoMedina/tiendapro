from django.shortcuts import redirect, render
from tiendapp.models import Customer, Product, ProductCategory
from tiendapp.models import OrderDetail, Order

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
    product_obj = Product.objects.get(sku = code)
    # request.user, guarda variable de sesion
    customer_obj = Customer.objects.get(user = request.user)

    orden_current = customer_obj.get_current_order()

    #Verifica si existe un producto seleccionado previamente
    detail_obj = OrderDetail.objects.filter(product = product_obj,
                            order = orden_current).first()
    
    if detail_obj is not None: # Actualiza price
        detail_obj.price = product_obj.price
        detail_obj.save()
    else: # Crear item en carrito
        detail_obj = OrderDetail()
        detail_obj.product = product_obj
        detail_obj.order = orden_current
        detail_obj.quantity = 1
        detail_obj.price = product_obj.price
        detail_obj.save()

    detail_obj = OrderDetail()

    return redirect("/cart")