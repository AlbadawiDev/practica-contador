# Práctica Contador

Este repositorio contiene el script **contador.py**, que:

- Pide al usuario un límite entero.
- Usa un bucle `for` para imprimir todos los números desde 1 hasta ese límite.
- Es útil para practicar la sintaxis de bucles en Python y la gestión de rangos.

## Uso

```bash
python contador.py

```

## Verificación local

Ejercicio de aprendizaje con funciones importables, validación de entrada y pruebas sin dependencias externas.

```powershell
python -X utf8 contador.py
python -X utf8 -m unittest discover -v
```

La entrada inválida devuelve código de salida 1 sin traceback. Las pruebas verifican límites y la consola.
