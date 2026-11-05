from pypdf import PdfReader

# Cambia esto por el nombre exacto de tu archivo PDF
nombre_archivo = "_ccredito_customerservice_impugnations_45297152902169497833 (1).pdf"
fecha_nacimiento = "19600722"

try:
    lector = PdfReader(nombre_archivo)
    
    if not lector.is_encrypted:
        print("El archivo no tiene contraseña.")
    else:
        print("Buscando el código postal... esto puede tardar un par de minutos.")
        
        # Probar todos los códigos postales del 00000 al 99999
        for i in range(100000):
            codigo_postal = str(i).zfill(5) # Rellena con ceros a la izquierda (ej. 01234)
            password = fecha_nacimiento + codigo_postal
            
            # Intentar desencriptar (devuelve un número > 0 si tiene éxito)
            if lector.decrypt(password) != 0:
                print("\n" + "="*40)
                print(f"¡ÉXITO! Contraseña encontrada: {password}")
                print(f"El código postal que usó el sistema es: {codigo_postal}")
                print("="*40 + "\n")
                break
                
            # Imprimir progreso cada 10,000 intentos para que veas que está trabajando
            if i > 0 and i % 10000 == 0:
                print(f"Probados {i} códigos...")
        else:
            print("No se encontró la contraseña. El formato podría ser distinto al esperado.")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{nombre_archivo}' en esta carpeta.")
except Exception as e:
    print(f"Ocurrió un error: {e}")