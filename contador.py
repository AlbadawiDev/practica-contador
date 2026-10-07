"""Cuenta desde uno sin ejecutar la consola al importar el módulo."""


def contar(limite):
    if limite < 0:
        raise ValueError("El límite debe ser cero o positivo.")
    return range(1, limite + 1)


def main():
    try:
        limite = int(input("Número hasta el que contar: "))
        for numero in contar(limite):
            print(numero)
    except (ValueError, EOFError):
        print("Entrada inválida: ingrese un entero cero o positivo.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
