from app.models import catalogo_productos

class CalculadorCotizacion:
    @staticmethod
    def calcular_subtotal(items_seleccionados):
        """Calcula el subtotal sumando los precios de los items seleccionados"""
        return sum(catalogo_productos[item] for item in items_seleccionados)
    
    @staticmethod
    def calcular_impuestos(subtotal, tasa_impuesto=0.19):
        """Calcula los impuestos basados en el subtotal y la tasa de impuesto"""
        return subtotal * tasa_impuesto
    
    @staticmethod
    def calcular_total(subtotal, impuestos, descuento=0):
        """Calcula el total final aplicando el descuento si existe"""
        total = subtotal + impuestos
        if descuento > 0:
            total *= (1 - descuento / 100)
        return total
    
    @staticmethod
    def calcular_cotizacion(cotizacion, tasa_impuesto=0.19):
        """Actualiza una cotización con todos los cálculos necesarios"""
        cotizacion.subtotal = CalculadorCotizacion.calcular_subtotal(cotizacion.items_seleccionados)
        cotizacion.impuestos = CalculadorCotizacion.calcular_impuestos(cotizacion.subtotal, tasa_impuesto)
        cotizacion.total = CalculadorCotizacion.calcular_total(cotizacion.subtotal, cotizacion.impuestos, cotizacion.descuento)
        return cotizacion