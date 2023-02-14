#Função para mostrar a torre
def torre(disco, origem, destino, auxiliar):
  if (disco == 1):
    print("Movendo o disco", disco, "da", origem, "para a", destino)
  else:
    torre(disco - 1, origem, auxiliar, destino)
    print("Movendo o disco", disco, "da", origem, "para a", destino)
    torre(disco - 1, auxiliar, destino, origem)


#Corpo principal
print("Usando a fórmula: 2^n - 1 podemos ver quantos movimentos minimos são necessários para completar a torre de Hanói.")
discos = int(input("Digite a quantidade de discos: "))
print("Precisariamos de", ((2**discos) - 1),"movimentos minimos para completar a torre com", discos, "discos.")
torre(discos, 'TORRE 1', 'TORRE 2', 'TORRE 3')
