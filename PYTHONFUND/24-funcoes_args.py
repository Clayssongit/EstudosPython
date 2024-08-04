"""
*args - Utilizamos ele quando não temos certeza de quantos argumentos queremos ter numa função.
- Os argumentos são passados como uma tupla

**Kwargs - além dos valores podemos passar também as respectivas chaves para cada argumento.
- Os argumentos são passados como um dicionário.
"""

# 1 - Soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")
sum(7,9,9,8)

# 2 - Apresentação de cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
presentation(name="Python", category="Backend", level="Iniciante")