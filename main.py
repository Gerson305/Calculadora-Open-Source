# calculadora

# Importamos las funciones de los diferentes archivos
from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import sumar_n_numeros

def mostrar_menu() -> None:
    """
    Muestra el menú principal de la calculadora
    """
    print("\n=== CALCULADORA ===")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar N números")
    print("6. Salir")
    print("=================")

def ejecutar_calculadora() -> None:
    """
    Función principal que ejecuta la calculadora
    """
    while True:
        mostrar_menu()
        try:
            opcion = int(input("\nSeleccione una opción (1-6): "))
            
            if opcion == 6:
                print("\n¡Gracias por usar la calculadora!")
                break
                
            if opcion < 1 or opcion > 6:
                print("\nError: Seleccione una opción válida (1-6)")
                continue
                
            # Opciones que requieren dos números
            if opcion in [1, 2, 3, 4]:
                try:
                    num1 = float(input("Ingrese el primer número: "))
                    num2 = float(input("Ingrese el segundo número: "))
                    
                    if opcion == 1:
                        resultado = sumar(num1, num2)
                        print(f"\nResultado: {num1} + {num2} = {resultado}")
                        
                    elif opcion == 2:
                        resultado = restar(num1, num2)
                        print(f"\nResultado: {num1} - {num2} = {resultado}")
                        
                    elif opcion == 3:
                        resultado = multiplicar(num1, num2)
                        print(f"\nResultado: {num1} × {num2} = {resultado}")
                        
                    elif opcion == 4:
                        resultado = dividir(num1, num2)
                        if resultado is not None:
                            print(f"\nResultado: {num1} ÷ {num2} = {resultado}")
                            
                except ValueError:
                    print("\nError: Ingrese solo números válidos")
                    
            # Opción de suma de N números
            elif opcion == 5:
                sumar_n_numeros()
                
            input("\nPresione Enter para continuar...")
                
        except ValueError:
            print("\nError: Ingrese una opción válida")
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    print("Bienvenido a la Calculadora")
    ejecutar_calculadora()
    print("¡Hasta luego!")