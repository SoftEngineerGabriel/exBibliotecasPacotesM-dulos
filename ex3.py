#3. Use o módulo string para verificar se uma string contém apenas dígitos.

import string

s = input("Digite uma string: ")

if all(c.isdigit() for c in s):
    print(f"A string '{s}' contém apenas dígitos.")
else:
    print(f"A string '{s}' não contém apenas dígitos.")