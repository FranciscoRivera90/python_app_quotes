import tkinter as tk
from tkinter import ttk, messagebox
from app.models import Cliente, Cotizacion, catalogo_productos
from app.calculations import CalculadorCotizacion
from app.pdf_generator import GeneradorPDF

class CotizacionGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.cotizacion = Cotizacion()
        self.inicializar_interfaz()
        
    def inicializar_interfaz(self):
        """Configura todos los elementos de la interfaz gráfica"""
        self.title("Aplicación de Cotizaciones")
        self.geometry("700x500")
        
        self.crear_seccion_cliente()
        self.crear_seccion_productos()
        self.crear_seccion_totales()
        self.crear_boton_pdf()
        
    def crear_seccion_cliente(self):
        """Crea la sección para ingresar datos del cliente"""
        frame_cliente = ttk.LabelFrame(self, text="Datos del Cliente")
        frame_cliente.pack(fill="x", padx=10, pady=5)
        
        ttk.Label(frame_cliente, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_nombre = ttk.Entry(frame_cliente, width=30)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame_cliente, text="Contacto:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_contacto = ttk.Entry(frame_cliente, width=30)
        self.entry_contacto.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame_cliente, text="Empresa:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_empresa = ttk.Entry(frame_cliente, width=30)
        self.entry_empresa.grid(row=2, column=1, padx=5, pady=5)
        
    def crear_seccion_productos(self):
        """Crea la sección para seleccionar productos y servicios"""
        frame_productos = ttk.LabelFrame(self, text="Seleccionar Productos/Servicios")
        frame_productos.pack(fill="x", padx=10, pady=5)
        
        self.lista_productos = tk.Listbox(frame_productos, selectmode=tk.MULTIPLE, height=5)
        for producto in catalogo_productos.keys():
            self.lista_productos.insert(tk.END, producto)
        self.lista_productos.pack(padx=5, pady=5)
        
        self.btn_agregar = ttk.Button(frame_productos, text="Agregar Seleccionados", command=self.agregar_items)
        self.btn_agregar.pack(pady=5)
        
    def crear_seccion_totales(self):
        """Crea la sección para mostrar totales y descuentos"""
        frame_totales = ttk.LabelFrame(self, text="Resumen Cotización")
        frame_totales.pack(fill="x", padx=10, pady=5)
        
        self.label_subtotal = ttk.Label(frame_totales, text="Subtotal: $0.00")
        self.label_subtotal.pack(pady=2)
        
        self.label_impuestos = ttk.Label(frame_totales, text="Impuestos (19%): $0.00")
        self.label_impuestos.pack(pady=2)
        
        self.label_total = ttk.Label(frame_totales, text="Total: $0.00", font=("Arial", 12, "bold"))
        self.label_total.pack(pady=5)
        
        ttk.Label(frame_totales, text="Descuento (%):").pack()
        self.entry_descuento = ttk.Entry(frame_totales, width=10)
        self.entry_descuento.pack(pady=2)
        
        self.btn_calcular = ttk.Button(frame_totales, text="Calcular Total", command=self.calcular_total)
        self.btn_calcular.pack(pady=5)
        
    def crear_boton_pdf(self):
        """Crea el botón para generar PDF"""
        self.btn_pdf = ttk.Button(self, text="Generar PDF", command=self.generar_pdf)
        self.btn_pdf.pack(pady=10)
        
    def agregar_items(self):
        """Agrega los productos seleccionados a la cotización"""
        seleccionados = self.lista_productos.curselection()
        items = [self.lista_productos.get(i) for i in seleccionados]
        self.cotizacion.items_seleccionados = items
        self.calcular_total()
        
    def calcular_total(self):
        """Calcula los totales y actualiza la interfaz"""
        # Actualizar cliente
        self.cotizacion.cliente.nombre = self.entry_nombre.get()
        self.cotizacion.cliente.contacto = self.entry_contacto.get()
        self.cotizacion.cliente.empresa = self.entry_empresa.get()
        
        # Obtener descuento
        descuento = self.entry_descuento.get()
        try:
            self.cotizacion.descuento = float(descuento) if descuento else 0
        except ValueError:
            messagebox.showerror("Error", "El descuento debe ser un número")
            self.entry_descuento.delete(0, tk.END)
            self.cotizacion.descuento = 0
            
        # Calcular totales
        CalculadorCotizacion.calcular_cotizacion(self.cotizacion)
        
        # Actualizar etiquetas
        self.label_subtotal.config(text=f"Subtotal: ${self.cotizacion.subtotal:.2f}")
        self.label_impuestos.config(text=f"Impuestos (19%): ${self.cotizacion.impuestos:.2f}")
        self.label_total.config(text=f"Total: ${self.cotizacion.total:.2f}")
        
    def generar_pdf(self):
        """Genera un PDF con la cotización"""
        # Validar datos
        if not self.cotizacion.cliente.nombre or not self.cotizacion.cliente.contacto or not self.cotizacion.cliente.empresa:
            messagebox.showerror("Error", "Debe completar todos los datos del cliente")
            return
            
        if not self.cotizacion.items_seleccionados:
            messagebox.showerror("Error", "Debe seleccionar al menos un producto")
            return
            
        # Actualizar cálculos por si acaso
        self.calcular_total()
        
        # Generar PDF
        try:
            filename = GeneradorPDF.generar_cotizacion_pdf(self.cotizacion)
            messagebox.showinfo("PDF Generado", f"Cotización guardada como {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el PDF: {str(e)}")