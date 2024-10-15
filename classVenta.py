class Venta:
    __id_venta = None
    __fecha = None
    __cliente = None
    __productos = None  # Diccionario de productos vendidos
    __total = None

    def __init__(self):
        self.__productos = {}
        self.__total = 0.0

    # Getters para acceder a los atributos privados
    def get_id_venta(self):
        return self.__id_venta

    def get_fecha(self):
        return self.__fecha

    def get_cliente(self):
        return self.__cliente

    def get_productos(self):
        return self.__productos

    def get_total(self):
        return self.__total

    # Setters para modificar los atributos privados
    def set_id_venta(self, id_venta):
        self.__id_venta = id_venta

    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_cliente(self, cliente):
        self.__cliente = cliente

    # Método para agregar productos al diccionario de productos
    def agregar_producto(self, nombre_producto, cantidad, precio_unitario):
        if nombre_producto in self.__productos:
            # Si el producto ya existe, solo actualiza la cantidad
            self.__productos[nombre_producto]['cantidad'] += cantidad
        else:
            # Si el producto no existe, se agrega al diccionario
            self.__productos[nombre_producto] = {'cantidad': cantidad, 'precio_unitario': precio_unitario}
        self.actualizar_total()

    # Método para calcular y actualizar el total
    def actualizar_total(self):
        self.__total = sum(
            producto['cantidad'] * producto['precio_unitario'] for producto in self.__productos.values()
        )

    # Método para mostrar los detalles de la venta
    def mostrar_detalle(self):
        print(f"ID Venta: {self.__id_venta}")
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente}")
        print("Productos vendidos:")
        for nombre, datos in self.__productos.items():
            print(f"{nombre}: Cantidad = {datos['cantidad']}, Precio Unitario = {datos['precio_unitario']}")
        print(f"Total: ${self.__total:.2f}")

# Uso de la clase Venta
venta = Venta()

# Configurando los datos de la venta
venta.set_id_venta(1001)
venta.set_fecha("2024-10-15")
venta.set_cliente("Cliente Ejemplo")

# Agregar productos a la venta
venta.agregar_producto("Producto A", 2, 50.25)
venta.agregar_producto("Producto B", 1, 25.50)
venta.agregar_producto("Producto C", 3, 15.00)

# Mostrar los detalles de la venta
venta.mostrar_detalle()
