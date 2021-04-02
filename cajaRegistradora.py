import unittest

class Producto():
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
    @property
    def codigo(self):
        return self.__codigo
    @property
    def nombre(self):
        return self.__nombre  
    @property
    def precioVenta(self):
        return self.__precio

class CajaRegistradora():

    def __init__(self):
        self.__productos = []
        self.__listaVenta = []
        self.__subtotal = 0
        self.__total = 0

    @property
    def productos(self):
        return self.__productos

    @property
    def lista_Venta(self):
        return self.__listaVenta    
    
    # se ingresan los productos a vender
    def registrar_producto(self, codigo, nombre, precio):
        nuevo = Producto (codigo, nombre, precio)
        self.__productos.append(nuevo)
    
    # se registra las ventas ingresando codigo del producto y la cantidad
    def venta (self, codigo, cantidad):
        for i in self.__productos:
            if i.codigo == codigo:
                precio = i.precioVenta * cantidad
                nombre = i.nombre
                self.__listaVenta.append((nombre,precio))

    # se suma los precios de la lista de la venta
    @property
    def subtotal(self):
        for lista in self.__listaVenta:
            self.__subtotal += lista[1]
        return self.__subtotal

    # el cambio del cliente
    def cambio_cliente(self, pagoCliente):
        total = self.precio_total
        cambio = pagoCliente - total
        return cambio 

    # precio total despues de descuentos
    # si compra 2 productos 10% de descuento
    # si compra 3 productos 20% de descuento
    # si compra 4 o mas 30% de decuento
    @property
    def precio_total(self):
        numProductos = len(self.__listaVenta)
        subtotal = self.subtotal
        if numProductos == 2:
            descuento = 0.1
        if numProductos == 3:
            descuento = 0.2
        if numProductos >= 4 :
            descuento = 0.3       
        self.__total = subtotal * (1 - descuento)
        return self.__total


# se realizan los test

class ProductoTest(unittest.TestCase):
    def setUp(self):
        self._producto = Producto(codigo="m4nz", nombre="Manzana", precio=4)
    def test_one_producto(self):
        codigo = self._producto.codigo
        self.assertEqual("m4nz", codigo)

    def test_two_producto(self):
        nombre = self._producto.nombre
        self.assertEqual("Manzana", nombre)

    def test_three_producto(self):
        precio = self._producto.precioVenta
        self.assertEqual(4,precio)            

class AlmacenTest(unittest.TestCase):
    def setUp(self):
        self._caja = CajaRegistradora()
        self._caja.registrar_producto("m4nz","Manzana",4)
        self._caja.registrar_producto("m3t0n","Melocoton",10)
        self._caja.registrar_producto("t0m4", "Tomate", 5 )
        self._caja.registrar_producto("b4n0","Banano", 8)
        
    def test_one_Venta (self):
        self._caja.venta(codigo="m4nz",cantidad=2)
        lista_de_venta = self._caja.lista_Venta
        self.assertListEqual([("Manzana",8)],lista_de_venta)
    
    def test_two_Venta (self):
        self._caja.venta(codigo="m4nz",cantidad=2)
        self._caja.venta(codigo="b4n0",cantidad=3)
        lista_de_venta = self._caja.lista_Venta
        self.assertListEqual([("Manzana",8),("Banano",24)],lista_de_venta)

    def test_three_venta(self):
        self._caja.venta(codigo="m4nz",cantidad=2)
        self._caja.venta(codigo="b4n0",cantidad=3)
        subTotal = self._caja.subtotal
        self.assertEqual(32, subTotal)
    
    def test_four_venta(self):
        self._caja.venta(codigo="m4nz",cantidad=2)
        self._caja.venta(codigo="b4n0",cantidad=3)
        total = self._caja.precio_total
        self.assertAlmostEqual(28.8, total)

    def test_five_venta(self):
        self._caja.venta(codigo="m4nz",cantidad=2)
        self._caja.venta(codigo="b4n0",cantidad=3)
        cambio = self._caja.cambio_cliente(30)
        self.assertAlmostEqual(1.2, cambio)

    def test_six_venta(self):
        self._caja.venta(codigo="m4nz",cantidad=2)
        self._caja.venta(codigo="b4n0",cantidad=3)
        self._caja.venta(codigo="t0m4",cantidad=4)
        total = self._caja.precio_total
        self.assertAlmostEqual(41.6, total)

    def test_seven_venta(self):
        self._caja.venta(codigo="m4nz",cantidad=2)
        self._caja.venta(codigo="b4n0",cantidad=3)
        self._caja.venta(codigo="t0m4",cantidad=6)
        self._caja.venta(codigo="m3t0n",cantidad=1)
        total = self._caja.precio_total
        self.assertAlmostEqual(50.4, total)    

if __name__== "__main__":
    unittest.main()
