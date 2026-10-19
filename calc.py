



def suma(num1: float, num2: float) -> float:
    """Da la suma de dos números"""
    return float(num1 + num2)

def resta(num1: float, num2: float) -> float:
    """Da la resta de dos números"""
    return float(num1 - num2)

def multiplicacion(num1: float, num2: float) -> float:
    """Da la multiplicación de dos números"""
    return float(num1 * num2)

def division(num1: float, num2: float) -> float:
    """Da la división de dos números"""
    return float(num1 / num2)


def main():
    """La función principal"""
    num1 = int(input("Dame un número: "))
    num2 = int(input("Dame otro número: "))

    print(f"La suma es {suma(num1, num2)}")
    print(f"La resta es {resta(num1, num2)}")
    print(f"La multiplicación es {multiplicacion(num1, num2)}")
    print(f"La división es {division(num1, num2)}")    

if __name__ == "__main__":
    main()

