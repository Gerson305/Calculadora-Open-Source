def dividir(a: float, b: float) -> float:
   
    try:
        if b == 0:
            raise ZeroDivisionError("No es posible dividir entre cero")
        return a / b
    except ZeroDivisionError as error:
        print(f"Error: {error}")
        return None

