# Aplicación de Cotizaciones Empresariales (README EN CONSTRUCCIÓN)

Una moderna aplicación de escritorio para generar, gestionar y exportar cotizaciones profesionales para clientes y prospectos comerciales.

## 📌 Tabla de Contenidos

- [Descripción General](#descripción-general)
- [Características Principales](#características-principales)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Componentes del Sistema](#componentes-del-sistema)
  - [models.py](#modelspy)
  - [calculations.py](#calculationspy)
  - [pdf_generator.py](#pdf_generatorpy)
  - [gui.py](#guipy)
  - [main.py](#mainpy)
- [Requisitos e Instalación](#requisitos-e-instalación)
  - [Requisitos del Sistema](#requisitos-del-sistema)
  - [Configuración del Entorno](#configuración-del-entorno)
  - [Instalación de Dependencias](#instalación-de-dependencias)
- [Guía de Uso](#guía-de-uso)
  - [Gestión de Clientes](#gestión-de-clientes)
  - [Selección de Productos](#selección-de-productos)
  - [Cálculo de Totales](#cálculo-de-totales)
  - [Generación de PDFs](#generación-de-pdfs)
- [Dockerización](#dockerización)
- [Contribución](#contribución)
- [Equipo de Desarrollo](#equipo-de-desarrollo)
- [Licencia](#licencia)

---

## 📖 Descripción General

La **Aplicación de Cotizaciones Empresariales** es una solución integral diseñada para optimizar el proceso comercial de empresas de cualquier tamaño. Esta herramienta permite a los representantes de ventas crear cotizaciones profesionales de manera rápida y sencilla, manteniendo una imagen corporativa consistente y garantizando cálculos precisos.

A diferencia de soluciones complejas de CRM, esta aplicación está enfocada específicamente en la generación de cotizaciones, lo que la hace extremadamente eficiente y fácil de usar para equipos comerciales.

## 🌟 Características Principales

✅ **Gestión de Clientes**: Captura y almacena datos esenciales de clientes y prospectos  
✅ **Catálogo de Productos**: Selección rápida desde un inventario predefinido  
✅ **Cálculos Automatizados**: Subtotales, impuestos y descuentos calculados instantáneamente  
✅ **Exportación PDF**: Documentos profesionales listos para enviar a clientes  
✅ **Interfaz Intuitiva**: Diseñada para minimizar errores y maximizar productividad  
✅ **Personalizable**: Adaptable a diferentes necesidades comerciales y regiones fiscales  

## 📂 Estructura del Proyecto

```
cotizacion-app/
│
├── main.py                   # Punto de entrada de la aplicación
├── models.py                 # Definición de clases y estructuras de datos
├── calculations.py           # Funciones para cálculos de cotizaciones
├── pdf_generator.py          # Generador de documentos PDF
├── gui.py                    # Interfaz gráfica de usuario
│
├── requirements.txt          # Dependencias del proyecto
├── Dockerfile                # Configuración para contenedorización
│
├── docs/                     # Documentación adicional
│   ├── manual_usuario.pdf
│   └── imagenes/
│       ├── pantalla_principal.png
│       └── ejemplo_pdf.png
│
└── tests/                    # Pruebas unitarias y de integración
    ├── test_models.py
    ├── test_calculations.py
    └── test_pdf_generator.py
```

## ⚙️ Componentes del Sistema

### `models.py`
Define las clases y estructuras de datos clave:
- **Cliente**: Almacena información de contacto
- **Cotizacion**: Contiene detalles de la cotización
- **catalogo_productos**: Diccionario con productos disponibles

```python
class Cliente:
    def __init__(self, nombre="", contacto="", empresa=""):
        self.nombre = nombre
        self.contacto = contacto
        self.empresa = empresa
```

### `calculations.py`
Realiza cálculos financieros:
- Subtotales
- Impuestos
- Descuentos
- Total final

```python
@staticmethod
def calcular_total(subtotal, impuestos, descuento=0):
    total = subtotal + impuestos
    if descuento > 0:
        total *= (1 - descuento / 100)
    return total
```

### `pdf_generator.py`
Genera documentos PDF usando **ReportLab**.

### `gui.py`
Interfaz gráfica desarrollada en **Tkinter**.

### `main.py`
Punto de entrada de la aplicación.

```python
from gui import CotizacionGUI

def main():
    app = CotizacionGUI()
    app.mainloop()

if __name__ == "__main__":
    main()
```

## 🛠 Requisitos e Instalación

### 📌 Requisitos del Sistema
- **Python 3.8+**
- **Tkinter** (incluido en la mayoría de instalaciones de Python)
- **Espacio en disco**: ~50MB
- **Sistemas operativos compatibles**: Windows, macOS, Linux

### 🔧 Configuración del Entorno

```bash
git clone https://github.com/su-empresa/cotizacion-app.git
cd cotizacion-app
python -m venv venv
```

Activar entorno virtual:
- **Windows**: `venv\Scripts\activate`
- **macOS/Linux**: `source venv/bin/activate`

### 📦 Instalación de Dependencias

```bash
pip install -r requirements.txt
```

## 📝 Guía de Uso

### 👥 Gestión de Clientes

```bash
python main.py
```
Ingrese datos del cliente en la interfaz.

### 📦 Selección de Productos
Seleccione productos del catálogo y agréguelos a la cotización.

### 🔢 Cálculo de Totales
El sistema calcula automáticamente subtotales, impuestos y descuentos.

### 📄 Generación de PDFs
Genere un archivo PDF con la cotización en un solo clic.

## 🐳 Dockerización

Construcción de la imagen:

```bash
docker build -t cotizacion-app:latest .
```

Ejecución del contenedor:

```bash
docker run -it cotizacion-app:latest
```

## 🤝 Contribución

1. **Haga fork del repositorio**
2. **Cree una rama** (`git checkout -b feature/nueva-caracteristica`)
3. **Implemente cambios y agregue pruebas**
4. **Envíe un pull request**

## 👨‍💻 Equipo de Desarrollo

- **Francisco Rivera** - Desarrollador FullStack

## 📜 Licencia

Proyecto bajo la licencia **MIT License**.

© 2025 [Excell PowerFull]. Todos los derechos reservados.
