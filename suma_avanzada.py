def sumar_n_numeros() -> float:
    
    try:
        # Solicitar la cantidad de números a sumar
        n = int(input("¿Cuántos números desea sumar? "))
        
        # Validar que N sea positivo
        if n <= 0:
            raise ValueError("La cantidad de números debe ser positiva")
        
        # Lista para almacenar los números
        numeros = []
        suma = 0
        
        # Solicitar cada número
        for i in range(n):
            numero = float(input(f"Ingrese el número {i+1}: "))
            numeros.append(numero)
            suma += numero
        
        # Mostrar los números ingresados y la suma
        print("\nNúmeros ingresados:", numeros)
        print(f"La suma total es: {suma}")
        
        return suma
        
    except ValueError as error:
        print(f"Error: Ingrese solo valores numéricos válidos")
        return None

