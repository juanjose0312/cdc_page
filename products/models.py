from django.db import models

CATEGORY_CHOICES = [
    ('espadin', 'Espadin'),
    ('control', 'Control'),
    ('bombillo', 'Bombillo'),
    ('carcasa', 'Carcasa'),
    ('mando', 'Mando'),
    ('sticker', 'Sticker'),
    ('vacio', 'Vacio'),
    ('llave', 'Llave'),
    ('pila', 'Pila'),
    ('chip', 'Chip'),
    ('botoneras', 'Botoneras'),
    ('logo', 'Logo'),
    ('goma', 'Goma')
]

BRAND_CHOICES = [
    ('Audi', 'Audi'),
    ('BMW', 'BMW'),
    ('Chevrolet', 'Chevrolet'),
    ('Chino', 'Chino'),
    ('Citroen', 'Citroen'),
    ('Cr Chery', 'Cr Chery'),
    ('Dodge-Jeep', 'Dodge-Jeep'),
    ('Energizer', 'Energizer'),
    ('Fiat', 'Fiat'),
    ('Ford', 'Ford'),
    ('Foton', 'Foton'),
    ('GP', 'GP'),
    ('Handy', 'Handy'),
    ('Hella', 'Hella'),
    ('Honda', 'Honda'),
    ('Hyundai', 'Hyundai'),
    ('Hyundai-Kia', 'Hyundai-Kia'),
    ('Kia', 'Kia'),
    ('Mazda', 'Mazda'),
    ('Mercedes', 'Mercedes'),
    ('Mitsubishi', 'Mitsubishi'),
    ('Murata', 'Murata'),
    ('Nissan', 'Nissan'),
    ('Onix', 'Onix'),
    ('Opel', 'Opel'),
    ('Originales', 'Originales'),
    ('Peugeot', 'Peugeot'),
    ('Q&Q', 'Q&Q'),
    ('Renault', 'Renault'),
    ('Sang Yong', 'Sang Yong'),
    ('Seat', 'Seat'),
    ('Skoda', 'Skoda'),
    ('Ssuo', 'Ssuo'),
    ('Suzuki', 'Suzuki'),
    ('Toyota', 'Toyota'),
    ('Volkswagen', 'Volkswagen'),
    ('Xhorse', 'Xhorse'),
    ('Yamaha', 'Yamaha'),
    ('Landrober', 'Landrober'),
    ('Keydiy-Peugeot', 'Keydiy-Peugeot'),
    ('Keydiy-Ford', 'Keydiy-Ford'),
    ('Keydiy', 'Keydiy'),
    ('Face to Face', 'Face to Face'),
    ('Keydiy-BMW', 'Keydiy-BMW')
]

# Create your models here.
class Product(models.Model):
    name =          models.TextField(max_length=200,verbose_name="name")
    category =      models.TextField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="categoria")
    filter_brand =  models.TextField(max_length=50, choices=BRAND_CHOICES, verbose_name="filtro_marca")
    filter_1 =      models.TextField(max_length=30, verbose_name="filtro_1")
    filter_2 =      models.TextField(max_length=30, null=True, verbose_name="filtro_2")
    filter_3 =      models.TextField(max_length=30, null=True, verbose_name="filtro_3")
    filter_4 =      models.TextField(max_length=90, null=True, verbose_name="filtro_4")
    cantidad =      models.IntegerField(verbose_name="cantidad")
    available =     models.BooleanField(default=True, verbose_name="disponible")
    id_catalog =    models.TextField(max_length=10, verbose_name="id_catalogo", primary_key=True)
    image =         models.ImageField(upload_to="images/",blank=True, null=True, verbose_name="imagen_catalogo")
    description =   models.TextField(max_length=255, null=True, verbose_name="descripcion_catalogo")
    retail_price =  models.DecimalField(max_digits=10, decimal_places=1, null=True, verbose_name="precio_unidad")
    wholesale_price=models.DecimalField(max_digits=10, decimal_places=1, null=True, verbose_name="precio_mayor")
    lacation_store =models.TextField(max_length=40, null=True, verbose_name="ubicacion_bodega")

    def save(self, *args, **kwargs):
        self.name = f"{self.category} {self.filter_brand} {self.filter_1} "
        self.available = self.cantidad > 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name