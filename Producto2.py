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


# Solicitar entrada de usuario para registrar productos
inventario = Inventario()

while True:
    id = int(input("Ingrese el ID del producto (0 para salir): "))
    if id == 0:
        break
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    costo = float(input("Ingrese el costo del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    producto = Producto(id, nombre, descripcion, costo, cantidad)
    margen_de_venta = float(input("Ingrese el margen de venta del producto: "))

    inventario.registrar_producto(producto, margen_de_venta)

print("Listado de Productos:")
inventario.imprimir_listado_productos()
