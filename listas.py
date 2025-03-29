# Removendo valor da lista
lista = [1,2,3,4,5]
print(lista)
lista.remove(2)
print(lista)
# Remove vc usa quando for remover um item certeiro, pois tem q passar qual será removido.
# metodo pop remove pelo indice.
lista.pop(3)
print(lista)

# METODO EXTENDS, JUNTA AS LISTAS.
lista.extend([6,7])
print(lista)

# Insert vc pode colocar um objeto definindo a posiçao dele
lista.insert(1,8)
print(lista)