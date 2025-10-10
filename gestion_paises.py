import csv

# Cargamos datos desde el archivo CSV:
def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        'nombre': fila['nombre'],
                        'poblacion': int(fila['poblacion']),
                        'superficie': int(fila['superficie']),
                        'continente': fila['continente'],
                        'idioma_principal': fila['idioma_principal'],
                        'moneda': fila['moneda'],
                        'capital': fila['capital'],
                        'clima': fila['clima']


                    }
                    paises.append(pais)
                except ValueError:
                    print(f"⚠️ Error de conversión en fila: {fila}")
    except FileNotFoundError:
        print("❌ Archivo no encontrado.")
    return paises

# Buscamos un país por nombre:
def buscar_pais(paises, nombre):
    return [pais for pais in paises if pais['nombre'].lower() == nombre.lower()]

# Filtramos por continente:
def filtrar_por_continente(paises, continente):
    return [pais for pais in paises if pais['continente'].lower() == continente.lower()]

# Filtramos por clima:
def filtrar_por_clima(paises, clima):
    return [p for p in paises if p['clima'].lower() == clima.lower()]


# Ordenamos por población o superficie:
def ordenar_paises(paises, clave, descendente=True):
    return sorted(paises, key=lambda x: x[clave], reverse=descendente)

# Estadísticas generales:
def estadisticas(paises):
    total_paises = len(paises)
    poblacion_total = sum(p['poblacion'] for p in paises)
    superficie_total = sum(p['superficie'] for p in paises)
    promedio_poblacion = poblacion_total / total_paises if total_paises else 0
    promedio_superficie = superficie_total / total_paises if total_paises else 0
    return {
        'total_paises': total_paises,
        'poblacion_total': poblacion_total,
        'superficie_total': superficie_total,
        'promedio_poblacion': promedio_poblacion,
        'promedio_superficie': promedio_superficie
    }

# Mostramos el menú:
def mostrar_menu():
    print("\n📊 Menú de Gestión de Países")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Ordenar por población")
    print("4. Ordenar por superficie")
    print("5. Ver estadísticas generales")
    print("6. Filtrar por clima")
    print("7. Salir")

# Programa principal:
def main():
    paises = cargar_paises('paises.csv')
    if not paises:
        return

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == '1':
            nombre = input("Nombre del país: ")
            resultado = buscar_pais(paises, nombre)
            print(resultado if resultado else "❌ País no encontrado.")
        elif opcion == '2':
            continente = input("Nombre del continente(América,Asia,África,Europa,Oceanía): ")
            resultado = filtrar_por_continente(paises, continente)
            print(f"{len(resultado)} países encontrados.")
            for p in resultado:
                print(p['nombre'])
        elif opcion == '3':
            ordenados = ordenar_paises(paises, 'poblacion')
            for p in ordenados[:5]:
                print(f"{p['nombre']}: {p['poblacion']} habitantes")
        elif opcion == '4':
            ordenados = ordenar_paises(paises, 'superficie')
            for p in ordenados[:5]:
                print(f"{p['nombre']}: {p['superficie']} km²")
        elif opcion == '5':
            stats = estadisticas(paises)
            print(f"🌍 Total de países: {stats['total_paises']}")
            print(f"👥 Población total: {stats['poblacion_total']}")
            print(f"📐 Superficie total: {stats['superficie_total']} km²")
            print(f"📊 Promedio de población: {int(stats['promedio_poblacion'])}")
            print(f"📊 Promedio de superficie: {int(stats['promedio_superficie'])} km²")
               

        elif opcion == '6':
            clima = input("Tipo de clima (Cálido, Frío, Templado, Tropical, Árido, Seco): ")
            resultado = filtrar_por_clima(paises, clima)
            if resultado:
              print(f"{len(resultado)} países con clima {clima}:")
              for p in resultado:
                 print(f"🌎 {p['nombre']}")
            else:
             print("❌ No se encontraron países con ese clima.")

        elif opcion == '7':
            print("👋 ¡Gracias por usar el sistema!")
            break
        else:
          print("⚠️ Opción inválida. Intenta nuevamente.")

    
if __name__ == "__main__":
    main()    

