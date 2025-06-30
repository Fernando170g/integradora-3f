import random
import json

tickets2 = {}

def mostrar_menu_principal():
    print("\n" + "="*50)
    print("        SISTEMA DE GESTIÓN DE TICKETS")
    print("="*50)
    print("1. Alta de ticket")
    print("2. Leer ticket")
    print("3. Salir")
    print("-"*50)

def alta_ticket():
    print("\n" + "="*40)
    print("        CREAR NUEVO TICKET")
    print("="*40)
    
 
    print("Por favor, ingrese los siguientes datos:")
    nombre = input("Nombre: ")
    sector = input("Sector: ")
    asunto = input("Asunto: ")
    problema = input("Problema: ")
    

    numero_ticket = random.randint(1000, 9999)
    

    while numero_ticket in tickets:
        numero_ticket = random.randint(1000, 9999)
    

    tickets[numero_ticket] = {
        'nombre': nombre,
        'sector': sector,
        'asunto': asunto,
        'problema': problema
    }
    
   
    print("\n" + "="*40)
    print("        TICKET CREADO EXITOSAMENTE")
    print("="*40)
    print(f"Número de ticket: {numero_ticket}")
    print(f"Nombre: {nombre}")
    print(f"Sector: {sector}")
    print(f"Asunto: {asunto}")
    print(f"Problema: {problema}")
    print("-"*40)
    print(f"¡IMPORTANTE! Recuerde su número de ticket: {numero_ticket}")
    print("-"*40)
    
  
    while True:
        respuesta = input("\n¿Desea crear otro ticket? (s/n): ").lower()
        if respuesta == 's' or respuesta == 'si':
            alta_ticket()
            break
        elif respuesta == 'n' or respuesta == 'no':
            break
        else:
            print("Por favor, ingrese 's' para sí o 'n' para no.")

def leer_ticket():
    print("\n" + "="*40)
    print("        CONSULTAR TICKET")
    print("="*40)
    
    if not tickets:
        print("No hay tickets registrados en el sistema.")
        input("Presione Enter para continuar...")
        return
    
    numero_ticket = input("Ingrese el número de ticket: ")
    
 
    if numero_ticket.isdigit():
        numero_ticket = int(numero_ticket)
        
        if numero_ticket in tickets:
            ticket = tickets[numero_ticket]
            print("\n" + "="*40)
            print("        INFORMACIÓN DEL TICKET")
            print("="*40)
            print(f"Número de ticket: {numero_ticket}")
            print(f"Nombre: {ticket['nombre']}")
            print(f"Sector: {ticket['sector']}")
            print(f"Asunto: {ticket['asunto']}")
            print(f"Problema: {ticket['problema']}")
            print("-"*40)
        else:
            print(f"No se encontró ningún ticket con el número {numero_ticket}")
    else:
        print("Por favor, ingrese un número de ticket válido.")
    

    while True:
        respuesta = input("\n¿Desea consultar otro ticket? (s/n): ").lower()
        if respuesta == 's' or respuesta == 'si':
            leer_ticket()
            break
        elif respuesta == 'n' or respuesta == 'no':
            break
        else:
            print("Por favor, ingrese 's' para sí o 'n' para no.")

def salir():
    print("\n" + "="*40)
    print("        CONFIRMAR SALIDA")
    print("="*40)
    
    while True:
        respuesta = input("¿Está seguro que desea salir del sistema? (s/n): ").lower()
        if respuesta == 's' or respuesta == 'si':
            print("\n¡Gracias por usar el sistema de gestión de tickets!")
            print("¡Que tenga un buen día!")
            return True
        elif respuesta == 'n' or respuesta == 'no':
            print("Regresando al menú principal...")
            return False
        else:
            print("Por favor, ingrese 's' para sí o 'n' para no.")

def main():
    print("¡Bienvenido al Sistema de Gestión de Tickets!")
    
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == '1':
            alta_ticket()
        elif opcion == '2':
            leer_ticket()
        elif opcion == '3':
            if salir():
                break
        else:
            print("\nOpción no válida. Por favor, seleccione una opción del 1 al 3.")
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    main()
with open ("tickets.json", "w") as tickets:
   json.dump(tickets2,tickets) 
