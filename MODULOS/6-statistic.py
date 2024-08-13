import statistics

# 1 - Aplicar a média 
print(statistics.mean([3, 2, 5, 9 ,1, 3]))

# 2 - Aplicar a mediana 
print(statistics.median([1, 2 , 3, 4, 5, 8, 9]))

# 3 - Aplicar a moda
print(statistics.mode([1, 2, 4, 3, 3, 3, 7, 6, 5, 4, 3, 2]))

# 4 - Desvio padrão 
"""
- Quanto mais próximo de 0 for o desvio padrão,
significado que os dados do conjunto estão menos dispersos
"""
print(statistics.stdev([1, 1.5, 1.5, 1.3, 3, 7 ]))