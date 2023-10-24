class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.precio_de_venta = None

    def registrar_precio_venta(self, margen_de_venta):
        if margen_de_venta > 0:
            self.precio_de_venta = self.costo / (1 - margen_de_venta)
        else:
            print("El margen de venta debe ser mayor que 0.")

class Inventario:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self, producto, margen_de_venta):
        producto.registrar_precio_venta(margen_de_venta)
        self.productos[producto.id] = producto

    def imprimir_listado_productos(self):
        for producto_id, producto in self.productos.items():
            print(f"ID: {producto_id}")
            print(f"Nombre: {producto.nombre}")
            print(f"Descripción: {producto.descripcion}")
            print(f"Costo: ${producto.costo}")
            print(f"Cantidad: {producto.cantidad}")
            if producto.precio_de_venta is not None:
                print(f"Precio de Venta: ${producto.precio_de_venta}")
            else:
                print("Precio de Venta no registrado.")
            print("\n")


producto1 = Producto(1, "hierbabuena", "Planta medicinal", 2500, 10)
producto2 = Producto(2, "Banano", "fruta alta en nutrientes", 600, 5)
producto3 = Producto(3, "Maracuya", "Fruta tropical", 3500,11)
producto4 = Producto(4, "Manzana", "Fruta tropical", 2000,4)
producto5 = Producto(5, "Limon", "Fruta tropical", 1000,14)


inventario = Inventario()
inventario.registrar_producto(producto1, 0.2)  # Asignar el margen de venta
inventario.registrar_producto(producto2, 0.25)  # Asignar el margen de venta
inventario.registrar_producto(producto3,0.3)
inventario.registrar_producto(producto4,0.2)
inventario.registrar_producto(producto5,0.1)

print("Listado de Productos:")
inventario.imprimir_listado_productos()

