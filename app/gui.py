import tkinter as tk
from tkinter import ttk, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class QuoteApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aplicación de Cotizaciones")
        self.geometry("700x500")

        # Diccionario de productos y precios
        self.productos = {
            "Producto A": 100.0,
            "Producto B": 200.0,
            "Servicio C": 150.0,
            "Servicio D": 300.0
        }
        self.items_seleccionados = []  # Lista para almacenar productos seleccionados

        # ================== Sección Cliente ==================
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

        # ================== Sección Productos ==================
        frame_productos = ttk.LabelFrame(self, text="Seleccionar Productos/Servicios")
        frame_productos.pack(fill="x", padx=10, pady=5)

        self.lista_productos = tk.Listbox(frame_productos, selectmode=tk.MULTIPLE, height=5)
        for producto in self.productos.keys():
            self.lista_productos.insert(tk.END, producto)
        self.lista_productos.pack(padx=5, pady=5)

        self.btn_agregar = ttk.Button(frame_productos, text="Agregar Seleccionados", command=self.agregar_items)
        self.btn_agregar.pack(pady=5)

        # ================== Sección Totales ==================
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

        # ================== Botón Generar PDF ==================
        self.btn_pdf = ttk.Button(self, text="Generar PDF", command=self.generar_pdf)
        self.btn_pdf.pack(pady=10)

    def agregar_items(self):
        """Agrega los productos seleccionados a la lista de cotización"""
        seleccionados = self.lista_productos.curselection()
        self.items_seleccionados = [self.lista_productos.get(i) for i in seleccionados]
        self.calcular_total()

    def calcular_total(self):
        """Calcula subtotal, impuestos y total final con descuento"""
        subtotal = sum(self.productos[item] for item in self.items_seleccionados)
        impuestos = subtotal * 0.19  # IVA del 19%
        total = subtotal + impuestos

        # Aplicar descuento si se ingresó
        descuento = self.entry_descuento.get()
        if descuento:
            try:
                descuento = float(descuento)
                total *= (1 - descuento / 100)
            except ValueError:
                messagebox.showerror("Error", "El descuento debe ser un número")

        # Actualizar etiquetas
        self.label_subtotal.config(text=f"Subtotal: ${subtotal:.2f}")
        self.label_impuestos.config(text=f"Impuestos (19%): ${impuestos:.2f}")
        self.label_total.config(text=f"Total: ${total:.2f}")

    def generar_pdf(self):
        """Genera un archivo PDF con la cotización"""
        cliente = self.entry_nombre.get()
        contacto = self.entry_contacto.get()
        empresa = self.entry_empresa.get()

        if not cliente or not contacto or not empresa or not self.items_seleccionados:
            messagebox.showerror("Error", "Debe completar todos los datos y seleccionar al menos un producto")
            return

        filename = "cotizacion.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        c.drawString(100, 750, f"Cliente: {cliente}")
        c.drawString(100, 730, f"Contacto: {contacto}")
        c.drawString(100, 710, f"Empresa: {empresa}")
        c.drawString(100, 680, "Productos Seleccionados:")

        y_position = 660
        for item in self.items_seleccionados:
            c.drawString(120, y_position, f"- {item}: ${self.productos[item]:.2f}")
            y_position -= 20

        subtotal = sum(self.productos[item] for item in self.items_seleccionados)
        impuestos = subtotal * 0.19
        total = subtotal + impuestos
        descuento = self.entry_descuento.get()
        if descuento:
            try:
                descuento = float(descuento)
                total *= (1 - descuento / 100)
            except ValueError:
                messagebox.showerror("Error", "El descuento debe ser un número")
                return

        c.drawString(100, y_position - 20, f"Subtotal: ${subtotal:.2f}")
        c.drawString(100, y_position - 40, f"Impuestos (19%): ${impuestos:.2f}")
        c.drawString(100, y_position - 60, f"Total: ${total:.2f}")

        c.save()
        messagebox.showinfo("PDF Generado", f"Cotización guardada como {filename}")

if __name__ == "__main__":
    app = QuoteApp()
    app.mainloop()
