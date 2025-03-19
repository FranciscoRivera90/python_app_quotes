from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from app.models import catalogo_productos

class GeneradorPDF:
    @staticmethod
    def generar_cotizacion_pdf(cotizacion, filename="cotizacion.pdf"):
        """Genera un archivo PDF con los detalles de la cotización"""
        c = canvas.Canvas(filename, pagesize=letter)
        
        # Información del cliente
        c.drawString(100, 750, f"Cliente: {cotizacion.cliente.nombre}")
        c.drawString(100, 730, f"Contacto: {cotizacion.cliente.contacto}")
        c.drawString(100, 710, f"Empresa: {cotizacion.cliente.empresa}")
        
        # Productos seleccionados
        c.drawString(100, 680, "Productos Seleccionados:")
        
        y_position = 660
        for item in cotizacion.items_seleccionados:
            c.drawString(120, y_position, f"- {item}: ${catalogo_productos[item]:.2f}")
            y_position -= 20
        
        # Totales
        c.drawString(100, y_position - 20, f"Subtotal: ${cotizacion.subtotal:.2f}")
        c.drawString(100, y_position - 40, f"Impuestos (19%): ${cotizacion.impuestos:.2f}")
        c.drawString(100, y_position - 60, f"Total: ${cotizacion.total:.2f}")
        
        # Si hay descuento, mostrarlo
        if cotizacion.descuento > 0:
            c.drawString(100, y_position - 80, f"Descuento aplicado: {cotizacion.descuento}%")
        
        c.save()
        return filename