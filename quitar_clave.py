from pypdf import PdfReader, PdfWriter

archivo_original = "_ccredito_customerservice_impugnations_45297152902169497833 (1).pdf"
password = "1960072275780"
archivo_nuevo = "Reporte_Limpio_Sin_Clave.pdf"

# Abrir y desencriptar
lector = PdfReader(archivo_original)
lector.decrypt(password)

# Crear un nuevo PDF en blanco
escritor = PdfWriter()

# Copiar todas las páginas al nuevo PDF
for pagina in lector.pages:
    escritor.add_page(pagina)

# Guardar el nuevo archivo sin contraseña
with open(archivo_nuevo, "wb") as f:
    escritor.write(f)

print(f"¡Listo! Se creó el archivo: {archivo_nuevo}")