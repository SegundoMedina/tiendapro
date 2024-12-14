from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tiendapp.models import Customer, Order, OrderDetail
from tiendapp.models import Product
# En PowerShell:
# python manage.py tienda_juanito

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("tienda tests")
        print("Comprando el MackBook Pro: ")
        mackbook = Product.objects.get(id = 2)
        print("> ", mackbook.name)

        print("Creando un Cliente: ")
        nuevo_user = User.objects.filter(username = "juanito.alcachofa@gmail.com").first()
        if nuevo_user is None:
            ### INICIO DE LA CREACION DE UN USUARIO
            nuevo_user = User()
            nuevo_user.first_name = "Juanito"
            nuevo_user.last_name = "Alcachofa"
            nuevo_user.username = "juanito.alcachofa@gmail.com"
            nuevo_user.is_active = True
            nuevo_user.save() # Almacena en base de datos al usuario

            nuevo_user.set_password("123456") # Definir contraseña
            nuevo_user.save()
            ### FIN DE LA CREACION DE UN USUARIO

        print("Enlazar el user al customer: ")
        nuevo_customer = Customer.objects.filter(user = nuevo_user).first()
        if nuevo_customer is None:
            nuevo_customer = Customer()
            nuevo_customer.user = nuevo_user # Enlace
            nuevo_customer.billing_address = "Av. Los lirios 43434"
            nuevo_customer.shipping_address = "Av. Colonial 2323"
            nuevo_customer.phone = "12121212"
            nuevo_customer.save()

        print("Creando una orden para el customer: ")
        nueva_order = Order.objects.filter(customer = nuevo_customer).first()
        if nueva_order is None:
            nueva_order = Order()
            nueva_order.customer = nuevo_customer
            nueva_order.shipping_address = nuevo_customer.shipping_address
            nueva_order.status = "PENDIENTE"
            nueva_order.save()





 