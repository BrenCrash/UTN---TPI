import csv
from collections import Counter

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

# Buscamos un país por nombre:coincidencia parcial o exacta, case-insensitive
def buscar_pais(paises, nombre):
    return [pais for pais in paises if nombre.lower() in pais['nombre'].lower()]

# Filtramos por continente:
def filtrar_por_continente(paises, continente):
    return [pais for pais in paises if pais['continente'].lower() == continente.lower()]

# Ordenamos por población, por superficie o por nombre del país:
def ordenar_paises(paises, clave, descendente=False):
    return sorted(paises, key=lambda x: x[clave], reverse=descendente)

# Filtramos por clima:
def filtrar_por_clima(paises, clima):
    return [p for p in paises if p['clima'].lower() == clima.lower()]

# Filtrar por rango de población (inclusive). min_poblacion/max_poblacion pueden ser None
def filtrar_por_poblacion(paises, min_poblacion=None, max_poblacion=None):
    resultado = []
    for p in paises:
        if (min_poblacion is None or p['poblacion'] >= min_poblacion) and \
           (max_poblacion is None or p['poblacion'] <= max_poblacion):
            resultado.append(p)
    return resultado

# Filtrar por rango de superficie (inclusive)
def filtrar_por_superficie(paises, min_superficie=None, max_superficie=None):
    resultado = []
    for p in paises:
        if (min_superficie is None or p['superficie'] >= min_superficie) and \
           (max_superficie is None or p['superficie'] <= max_superficie):
            resultado.append(p)
    return resultado

# Estadísticas generales y particulares:
def estadisticas(paises):
    total_paises = len(paises)
    poblacion_total = sum(p['poblacion'] for p in paises)
    superficie_total = sum(p['superficie'] for p in paises)
    promedio_poblacion = poblacion_total / total_paises if total_paises else 0
    promedio_superficie = superficie_total / total_paises if total_paises else 0
    pais_mayor_pob = max(paises, key=lambda x: x['poblacion'])
    pais_menor_pob = min(paises, key=lambda x: x['poblacion'])
    continentes = [p['continente'] for p in paises]
    cantidad_por_continente = dict(Counter(continentes))
    return {
        'total_paises': total_paises,
        'poblacion_total': poblacion_total,
        'superficie_total': superficie_total,
        'promedio_poblacion': promedio_poblacion,
        'promedio_superficie': promedio_superficie,
        'pais_mayor_poblacion': pais_mayor_pob,
        'pais_menor_poblacion': pais_menor_pob,
        'cantidad_por_continente': cantidad_por_continente
    }

# Lectura de enteros opcionales
def leer_entero_opcional(prompt):
    entrada = input(prompt).strip()
    if entrada == '':
        return None
    try:
        return int(entrada)
    except ValueError:
        print("⚠️ Valor inválido, por favor ingrese números enteros y reinicie el programa.")
        return None

# Mostramos el menú:
def mostrar_menu():
    print("\n📊 Menú de Gestión de Países:")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Ordenar por población")
    print("4. Ordenar por superficie")
    print("5. Ordenar por nombre")
    print("6. Filtrar por clima")
    print("7. Filtrar por rango de población")
    print("8. Filtrar por rango de superficie")
    print("9. Ver estadísticas generales y particulares")
    print("10.Salir")

# Programa principal:
def main():
    paises = cargar_paises('paises.csv')
    if not paises:
        return

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")
        if opcion == '1':
            nombre = input("\nNombre del país: ")
            resultado = buscar_pais(paises, nombre)
            print(resultado if resultado else "❌ País no encontrado.")
        elif opcion == '2':
            continente = input("\nNombre del continente(América, Asia, África, Europa, Oceanía): ")
            resultado = filtrar_por_continente(paises, continente)
            print(f"{len(resultado)} países encontrados.")
            for p in resultado:
                print(p['nombre'])
        elif opcion == '3':
            print("")
            ordenados = ordenar_paises(paises, 'poblacion')
            for p in ordenados:
                print(f"{p['nombre']}: {p['poblacion']} habitantes")
        elif opcion == '4':
            print("")
            ordenados = ordenar_paises(paises, 'superficie')
            for p in ordenados:
                print(f"{p['nombre']}: {p['superficie']} km²")
        elif opcion == '5':
            print("")
            ordenados = ordenar_paises(paises, 'nombre')
            for p in ordenados:
                print(f"{p['nombre']}")        
        elif opcion == '6':
            clima = input("\nTipo de clima (Cálido, Frío, Templado, Tropical, Árido, Seco): ")
            resultado = filtrar_por_clima(paises, clima)
            if resultado:
              print(f"{len(resultado)} países con clima {clima}:")
              for p in resultado:
                 print(f"🌎 {p['nombre']}")
            else:
             print("❌ No se encontraron países con ese clima.")
        elif opcion == '7':
            min_p = leer_entero_opcional("\nPoblación mínima: ")
            if min_p == None:
                break
            max_p = leer_entero_opcional("Población máxima: ")
            if max_p == None:
                break
            resultados = filtrar_por_poblacion(paises, min_p, max_p)
            print(f"🔎 {len(resultados)} países encontrados en rango de población:")
            for p in resultados:
                print(f"- {p['nombre']}: {p['poblacion']} habitantes")
        elif opcion == '8':
            min_s = leer_entero_opcional("\nSuperficie mínima (km²): ")
            if min_s == None:
                break
            max_s = leer_entero_opcional("Superficie máxima (km²): ")
            if max_s == None:
                break
            resultados = filtrar_por_superficie(paises, min_s, max_s)
            print(f"🔎 {len(resultados)} países encontrados en rango de superficie:")
            for p in resultados:
                print(f"- {p['nombre']}: {p['superficie']} km²")
        elif opcion == '9':
            stats = estadisticas(paises)
            print(f"\n🌍 Total de países: {stats['total_paises']}")
            print(f"👥 Población total: {stats['poblacion_total']}")
            print(f"📐 Superficie total: {stats['superficie_total']} km²")
            print(f"📊 Promedio de población: {int(stats['promedio_poblacion'])}")
            print(f"📊 Promedio de superficie: {int(stats['promedio_superficie'])} km²")
            if stats['pais_mayor_poblacion']:
                pm = stats['pais_mayor_poblacion']
                print(f"🏆 País con mayor población: {pm['nombre']} ({pm['poblacion']})")
            if stats['pais_menor_poblacion']:
                pmn = stats['pais_menor_poblacion']
                print(f"🔻 País con menor población: {pmn['nombre']} ({pmn['poblacion']})")
            print("📍 Cantidad de países por continente:")
            for cont, cnt in stats['cantidad_por_continente'].items():
                print(f"- {cont}: {cnt}")
        elif opcion == '10':
            print("\n👋 ¡Gracias por usar el sistema!")
            break
        else:
          print("⚠️ Opción inválida. Intenta nuevamente.")

    
if __name__ == "__main__":
    main()    

