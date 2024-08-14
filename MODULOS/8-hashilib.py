import hashlib

# 1 - Verificar os algoritmos disponíveis
print(hashlib.algorithms_available)

# 2 - Algoritmos disponiveis de acordo com o SO
print(hashlib.algorithms_available)

# 3 - Utilizando o Sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = " A melhor forma de prever o futuro é criá-lo".encode() # o enconde é utilizado para converter uma string em uma sequência de bytes
algorithm.update(message)
print(algorithm.hexdigest())

# 4 - Uitilizando o MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())