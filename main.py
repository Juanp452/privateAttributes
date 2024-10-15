from classVenta import Venta

# Crear una instancia de la clase Venta
venta = Venta()

# Configurando los datos de la venta
venta.set_id_venta(1)
venta.set_fecha("15/10/2024")
venta.set_cliente("Juanp")

# Agregar productos con su nombre, cantidad y precio unitario
venta.agregar_producto("Producto1", 2, 50.25)
venta.agregar_producto("Producto2", 1, 25.50)
venta.agregar_producto("Producto3", 3, 15.00)

# Mostrar los detalles de la venta
venta.mostrar_detalle()
