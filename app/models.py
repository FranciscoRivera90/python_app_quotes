class Cliente:
    def __init__(self, nombre="", contacto="", empresa=""):
        self.nombre = nombre
        self.contacto = contacto
        self.empresa = empresa

class Cotizacion:
    def __init__(self):
        self.cliente = Cliente()
        self.items_seleccionados = []
        self.descuento = 0
        self.subtotal = 0
        self.impuestos = 0
        self.total = 0
        
    def agregar_item(self, item):
        if item not in self.items_seleccionados:
            self.items_seleccionados.append(item)
            
    def agregar_items(self, items):
        for item in items:
            self.agregar_item(item)
            
    def limpiar_items(self):
        self.items_seleccionados = []

# Catálogo de productos disponibles (podría cargarse desde una base de datos en un caso real)
catalogo_productos = {
    "Producto A": 100.0,
    "Producto B": 200.0,
    "Servicio C": 150.0,
    "Servicio D": 300.0
}